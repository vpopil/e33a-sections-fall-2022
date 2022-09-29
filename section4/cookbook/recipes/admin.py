from django.contrib import admin

from .models import Category, Recipe, Ingredient

# Register your models here.

class IngredientInline(admin.StackedInline):
    model = Ingredient.recipes.through
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]

class IngredientAdmin(admin.ModelAdmin):
    filter_horizontal = ("recipes",)

admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)

#
# class RecipeAdmin(admin.ModelAdmin):
#     filter_horizontal = ("ingredients",)
#
# class IngredientAdmin(admin.ModelAdmin):
#     filter_horizontal = ("recipe",)
#
#
# admin.site.register(Category)
# admin.site.register(Recipe, RecipeAdmin)
# admin.site.register(Ingredient)#, IngredientAdmin)
