from django import forms
from .models import Ingredient, MenuItem, RecepyRequirement, Purchase


class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"


class MenuItemUpdateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"


class RecepyRequirementCreateForm(forms.ModelForm):
    class Meta:
        model = RecepyRequirement
        fields = ("ingredient", "quantity")


class RecepyRequirementUpdateForm(forms.ModelForm):
    class Meta:
        model = RecepyRequirement
        fields = ("ingredient", "quantity")


class RecepyRequirementForm(forms.ModelForm):
    class Meta:
        model = RecepyRequirement
        fields = "__all__"


class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(PurchaseCreateForm, self).__init__(*args, **kwargs)
        self.fields['menu_item'].queryset = MenuItem.available_objects.all()


class PurchaseUpdateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"


class PurchaseForm(forms.ModelForm):
    class meta:
        model = Purchase
        fields = "__all__"
