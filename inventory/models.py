from django.db import models
from datetime import datetime
from django.utils.timezone import make_aware


class PurchaseManager(models.Manager):
    """ Class to extend the Purchase model
    """
    def total_revenue(self):
        """ Calculate Total Revenue
        """
        total = 0
        purchases = Purchase.objects.all()
        for purchase in purchases:
            total += purchase.menu_item.price
        return total

    def total_cost(self):
        """ Calculate Total Cost
        """
        total = 0
        purchases = Purchase.objects.all()
        for purchase in purchases:
            total += purchase.menu_item.calculate_cost()
        return total

    def total_profit(self):
        """ Calculate total Profit
        """
        return self.total_revenue() - self.total_cost()


class AvailableMenuItemManager(models.Manager):
    """
    Class to be able to query only available ManuItems
    """
    def get_queryset(self):
        menu_items = MenuItem.objects.all()
        print(menu_items)
        print(menu_items[0].available())
        available_items = [item.id for item in menu_items if item.available()]
        print(available_items)
        return super().get_queryset().filter(id__in=available_items)




# Create your models here.
class Ingredient(models.Model):
    """ Class defining the ingredient model.
    An ingredient has a name, quantity, unit and unit_price
    """
    name = models.CharField(max_length=40)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=10)
    unit_price = models.FloatField(default=1.)

    def __str__(self):
        return self.name + " with a stock of {} ".format(self.quantity) + self.unit


class MenuItem(models.Model):
    """ Class defining the entries on the menu.
    """
    title = models.CharField(max_length=40, unique=True)
    price = models.FloatField(default=1.)

    def __str__(self):
        return self.title + " with a price of {}".format(self.price)

    # Include some usefull methods to make queries easier
    def calculate_cost(self):
        """ Calculate cost based on price of required ingredients
        """
        cost = 0
        requirements = self.recepyrequirement_set.all()
        for requirement in requirements:
            cost += requirement.quantity * requirement.ingredient.unit_price
        return cost

    def calculate_profit(self):
        """ Calculate profit based on cost and menu price
        """
        cost = self.calculate_cost()
        profit = self.price - cost
        return profit

    def available(self):
        """ Check if enough quantity of all required ingredients is available
        """
        available = True
        requirements = self.recepyrequirement_set.all()
        for requirement in requirements:
            if requirement.quantity > requirement.ingredient.quantity:
                available = False
        return available

    # Normally we want all objects, but we want to be able to query
    # available objects using a different method.
    objects = models.Manager()
    available_objects = AvailableMenuItemManager()

    def purchase(self):
        if self.available():
            requirements = self.recepyrequirement_set.all()
            for requirement in requirements:
                actual = requirement.ingredient.quantity
                new = actual - requirement.quantity
                requirement.ingredient.quantity = new
                requirement.ingredient.save()
            bought = Purchase(menu_item=self)
            bought.save()
        else:
            raise ResourceWarning("Not enough ingredients available!")


class RecepyRequirement(models.Model):
    """ Keep track of the ingredient requirements for all recepies.
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=1.)

    def __str__(self):
        return (self.menu_item.title + " requires {} of ".format(self.quantity)
                + self.ingredient.name)


class Purchase(models.Model):
    """ Class to keep track of what customers have purchased
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=make_aware(datetime.now()))

    def __str__(self):
        return self.menu_item.title + " was purchased at {}".format(self.timestamp)

    objects = PurchaseManager()
