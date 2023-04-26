from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from .models import Ingredient, MenuItem, RecepyRequirement, Purchase
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView


# Start to create views here
class HomeView(TemplateView):
    template_name = "inventory/home.html"


# Create your views here.
class MenuItemView(ListView):
    model = MenuItem
    template_name = "inventory/menuitems.html"
