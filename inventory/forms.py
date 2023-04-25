from django import forms
from .models import Ingredient, MenuItem, RecepyRequirement, Purchase


class IngredientCreateForm(forms.Form):
    class meta:
        model = Ingredient
        fields = ["name", "quantity", "unit", "unit_price"]
