from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Step, Ingredient, Recipe


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class Ingredient(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass
