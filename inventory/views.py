from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse, reverse_lazy
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
    template_name = "inventory/menuitems.html"
    form_class = MenuItemForm


class MenuItemCreateView(CreateView):
    model = MenuItem
    template_name = "inventory/create_menuitem.html"
    form_class = MenuItemCreateForm


class MenuItemUpdateView(UpdateView):
    model = MenuItem
    template_name = "inventory/update_menuitem.html"
    form_class = MenuItemUpdateForm


class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = "inventory/delete_menuitem.html"
    success_url = "/inventory/menu_items/"


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
def recepyrequirementview(request, menu_item_title):
    return Http404


class RecepyRequirementCreateView(CreateView):
    model = RecepyRequirement
    template_name = "inventory/create_recepyrequirement.html"
    form_class = RecepyRequirementCreateForm


class RecepyRequirementUpdateView(UpdateView):
    model = RecepyRequirement
    template_name = "inventory/update_recepyrequirement.html"
    form_class = RecepyRequirementUpdateForm


class RecepyRequirementDeleteView(DeleteView):
    model = Ingredient
    template_name = "inventory/delete_recepyrequirement.html"
    success_url = "/inventory/menu_items/"


# Now do the views related to the Purchase s
class PurchaseView(ListView):
    model = Purchase
    template_name = "inventory/purchases.html"
    context_object_name = "purchases"


class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = "inventory/create_purchase.html"
    form_class = PurchaseCreateForm
    success_url = reverse_lazy("purchases")



class PurchaseUpdateView(UpdateView):
    model = Purchase
    template_name = "inventory/update_purchase.html"
    form_class = PurchaseUpdateForm
    success_url = reverse_lazy("purchases")


class PurchaseDeleteView(DeleteView):
    model = Purchase
    template_name = "inventory/delete_purchase.html"
    success_url = reverse_lazy("purchases")
