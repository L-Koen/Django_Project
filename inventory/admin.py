from django.contrib import admin

from .models import Ingredient, MenuItem, RecepyRequirement, Purchase

admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecepyRequirement)
admin.site.register(Purchase)
