from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Ingredient, MenuItem, RecepyRequirement, Purchase
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .forms import *


# Start to create views here
# First the Homeview
class HomeView(TemplateView):
    template_name = "inventory/home.html"


# Now do the views related to the MenuItem s
class MenuItemView(ListView):
    model = MenuItem
    template_name = "inventory/menu_items.html"
    form_class = MenuItemForm
    context_object_name = "menu_items"


class MenuItemCreateView(CreateView):
    model = MenuItem
    template_name = "inventory/create_menu_item.html"
    form_class = MenuItemCreateForm
    success_url = reverse_lazy("menu_items")


class MenuItemUpdateView(UpdateView):
    model = MenuItem
    template_name = "inventory/update_menu_item.html"
    form_class = MenuItemUpdateForm
    success_url = reverse_lazy("menu_items")


class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = "inventory/delete_menu_item.html"
    success_url = reverse_lazy("menu_items")


# Now do the views related to the Ingredient s
class IngredientView(ListView):
    model = Ingredient
    template_name = "inventory/ingredients.html"
    context_object_name = "ingredients"


class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = "inventory/create_ingredient.html"
    form_class = IngredientCreateForm
    success_url = reverse_lazy('ingredients')


class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = "inventory/update_ingredient.html"
    form_class = IngredientUpdateForm
    success_url = reverse_lazy('ingredients')


class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "inventory/delete_ingredient.html"
    success_url = reverse_lazy('ingredients')


# Now do the views related to the RecipyRequirement s
# Requirement vie will be different, as I want to view requirements by recepy
def recepyrequirementview(request, menupk):
    context = {}
    menu_item = MenuItem.objects.get(id=menupk)
    requirements = menu_item.recepyrequirement_set.all()
    context["requirements"] = requirements
    context["menu_item"] = menu_item
    return render(request, "inventory/recepy_requirements.html", context)


class RecepyRequirementCreateView(CreateView):
    model = RecepyRequirement
    template_name = "inventory/create_recepyrequirement.html"
    form_class = RecepyRequirementCreateForm
    success_url = reverse_lazy('menu_items')

    # To create it for a certain menu_item, we have to restrict ourselves
    # to that item.
    def dispatch(self, request, *args, **kwargs):
        """ First get MenuItem
        """
        self.menu_item = get_object_or_404(MenuItem, pk=kwargs["menupk"])
        return super(RecepyRequirementCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.menu_item = self.menu_item
        return super().form_valid(form)


class RecepyRequirementUpdateView(UpdateView):
    model = RecepyRequirement
    template_name = "inventory/update_recepyrequirement.html"
    form_class = RecepyRequirementUpdateForm
    success_url = reverse_lazy('menu_items')


class RecepyRequirementDeleteView(DeleteView):
    model = RecepyRequirement
    template_name = "inventory/delete_recepyrequirement.html"
    success_url = reverse_lazy('menu_items')


# Now do the views related to the Purchase s
class PurchaseView(ListView):
    model = Purchase
    template_name = "inventory/purchases.html"
    context_object_name = "purchases"


class PurchaseCreateView(CreateView):
    """ Class to create purchases.
    After validation menu_item.purchase() is called to update inventory.
    In order to do so, the form_valid function is extended.
    Remember, PurchaseCreateForm will only show us MenuItems for which the ingredients are available
    """
    model = Purchase
    template_name = "inventory/create_purchase.html"
    form_class = PurchaseCreateForm
    success_url = reverse_lazy("purchases")

    def form_valid(self, form):
        super(PurchaseCreateView, self).form_valid(form)
        form.cleaned_data['menu_item'].purchase()
        messages.success(self.request, 'Item purchased successfully!')
        return HttpResponseRedirect(self.get_success_url())


class PurchaseUpdateView(UpdateView):
    model = Purchase
    template_name = "inventory/update_purchase.html"
    form_class = PurchaseUpdateForm
    success_url = reverse_lazy("purchases")


class PurchaseDeleteView(DeleteView):
    model = Purchase
    template_name = "inventory/delete_purchase.html"
    success_url = reverse_lazy("purchases")


def financial(request):
    context = {}
    context["profit"] = Purchase.objects.total_profit()
    context["revenue"] = Purchase.objects.total_revenue()
    context["cost"] = Purchase.objects.total_cost()
    return render(request, "inventory/financial.html", context)
