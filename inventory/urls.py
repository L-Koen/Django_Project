from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    # urls for Ingredients
    path("ingredients/", views.IngredientView.as_view(), name="ingredients"),

    # urls for Purchases
    path("purchases/", views.PurchaseView.as_view(), name="purchases"),

    # urls for MenuItems
    path("menu_items/", views.MenuItemView.as_view(), name="menu_items"),

    # urls for RecepyRequirements
    path("recepy_requirement/<str:menu_item_title>/", views.recepyrequirementview, name="requirement"),
]
