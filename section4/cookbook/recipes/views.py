from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Recipe, Ingredient
from django.forms import ModelForm


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'price']  # For listing no User please

# Create your views here.
def index(request):
    context = {
        "recipes": Recipe.objects.all()
    }
    return render(request, "recipes/index.html", context)


def recipe(request, recipe_id):
    i = 0

    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    context = {
        "recipe": recipe,
        "ingredients": recipe.ingredients.all(),
        "non_ingredients": Ingredient.objects.exclude(recipes=recipe).all()
    }
    return render(request, "recipes/recipe.html", context)


def add(request, recipe_id):
    try:
        ingredient_id = int(request.POST["ingredient"])
        recipe = Recipe.objects.get(pk=recipe_id)
        ingredient = Ingredient.objects.get(pk=ingredient_id)
    except KeyError:
        return render(request, "recipes/error.html", {"message": "No selection."})
    except Recipe.DoesNotExist:
        return render(request, "recipes/error.html", {"message": "No recipe."})
    except Ingredient.DoesNotExist:
        return render(request, "recipes/error.html", {"message": "No ingredient."})

    # associate with recipe
    ingredient.recipes.add(recipe)

    # recipe.ingredients.add(recipe)

    return HttpResponseRedirect(reverse("recipe", args=(recipe_id,)))


def ingredient(request):
    if request.method == 'POST':
        ingredient_form = IngredientForm(request.POST)

        if ingredient_form.is_valid():

            # ingredient_object = ingredient_form.save(commit=False)
            # ingredient_object.seller = request.user
            ingredient_form.save()
            return HttpResponseRedirect(reverse("index"))
        # else:
        #     return render(request, "recipes/ingredient.html", {'form': IngredientForm(intial={'name':__, 'price':___})})
            

    return render(request, "recipes/ingredient.html", {'form': IngredientForm()})

