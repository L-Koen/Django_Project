from django import forms
from .models import Ingredient, MenuItem, RecepyRequirement, Purchase


class IngredientCreateForm(forms.Form):
    class meta:
        model = Ingredient
        fields = "__all__"


class IngredientUpdateForm(forms.form):
    class meta:
        model = Ingredient
        fields = ["quantity", "unit_price"]


class IngredientForm(forms.Form):
    class meta:
        model = Ingredient
        fields = "__all__"


class MenuItemCreateForm(forms.Form):
    class meta:
        model = MenuItem
        fields = "__all__"


class MenuItemUpdateForm(forms.Form):
    class meta:
        model = MenuItem
        fields = "__all__"


class MenuItemForm(forms.Form):
    class meta:
        model = MenuItem
        fields = "__all__"


class RecepyRequirementCreateForm(forms.Form):
    class meta:
        model = RecepyRequirement
        fields = "__all__"


class RecepyRequirementUpdateForm(forms.Form):
    class meta:
        model = RecepyRequirement
        fields = "__all__"


class RecepyRequirementForm(forms.Form):
    class meta:
        model = RecepyRequirement
        fields = "__all__"


class PurchaseCreateForm(forms.Form):
    class meta:
        model = Purchase
        fields = "__all__"


class PurchaseUpdateForm(forms.Form):
    class meta:
        model = Purchase
        fields = "__all__"


class PurchaseForm(forms.Form):
    class meta:
        model = Purchase
        fields = "__all__"
