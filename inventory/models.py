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
            total += purchase.menu_item.calculate_cost(purchase.menu_item)
        return total

    def total_profit(self):
        """ Calculate total Profit
        """
        return self.total_revenue() - self.total_cost()


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
    def calculate_cost(self, menu_item):
        """ Calculate cost based on price of required ingredients
        """
        cost = 0
        requirements = menu_item.recepyrequirement_set.all()
        for requirement in requirements:
            cost += requirement.quantity * requirement.ingredient.unit_price
        return cost

    def calculate_profit(self, menu_item):
        """ Calculate profit based on cost and menu price
        """
        cost = menu_item.calculate_cost(menu_item)
        profit = menu_item.price - cost
        return profit

    def available(self, menu_item):
        """ Check if enough quantity of all required ingredients is available
        """
        available = True
        requirements = menu_item.recepyrequirement_set.all()
        for requirement in requirements:
            if requirement.quantity > requirement.ingredient.quantity:
                available = False
        return available

    def purchase(self, menu_item):
        if menu_item.available(menu_item):
            requirements = menu_item.recepyrequirement_set.all()
            for requirement in requirements:
                actual = requirement.ingredient.quantity
                new = actual - requirement.quantity
                requirement.ingredient.quantity = new
                requirement.ingredient.save()
            bought = Purchase(menu_item=menu_item)
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
