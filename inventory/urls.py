from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    # urls for Ingredients
    path("ingredients/", views.IngredientView.as_view(), name="ingredients"),
    path("ingredients/create", views.IngredientCreateView.as_view(), name="ingredient_create"),
    path("ingredients/delete/<pk>", views.IngredientDeleteView.as_view(), name="ingredient_delete"),
    path("ingredients/update/<pk>", views.IngredientUpdateView.as_view(), name="ingredient_update"),

    # urls for Purchases
    path("purchases/", views.PurchaseView.as_view(), name="purchases"),
    path("purchases/create", views.PurchaseCreateView.as_view(), name="purchase_create"),
    path("purchases/delete/<pk>", views.PurchaseDeleteView.as_view(), name="purchase_delete"),
    path("purchases/update/<pk>", views.PurchaseUpdateView.as_view(), name="purchase_update"),

    # urls for MenuItems
    path("menu_items/", views.MenuItemView.as_view(), name="menu_items"),
    path("menu_items/create", views.MenuItemCreateView.as_view(), name="menu_item_create"),
    path("menu_items/update/<pk>", views.MenuItemUpdateView.as_view(), name="menu_item_update"),
    path("menu_items/delete/<pk>", views.MenuItemDeleteView.as_view(), name="menu_item_delete"),

    # urls for RecepyRequirements
    path("recepy_requirement/requirement/<int:menupk>/", views.recepyrequirementview, name="requirement"),
    path("recepy_requirement/requirement/create/<int:menupk>/", views.RecepyRequirementCreateView.as_view(), name="requirement_create"),
    path("recepy_requirement/requirement/update/<pk>/", views.RecepyRequirementUpdateView.as_view(), name="requirement_update"),
    path("recepy_requirement/requirement/delete/<pk>/", views.RecepyRequirementDeleteView.as_view(), name="requirement_delete"),

    # url for financial
    path("financial/", views.financial, name="financial"),
]
