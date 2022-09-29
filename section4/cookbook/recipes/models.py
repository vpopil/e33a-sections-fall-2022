from email.policy import default
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"

# cat = Category.get(pk=1)
# cat.receipes.all()


class Recipe(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="receipes")
    prep_time = models.IntegerField() # in minutes

    def __str__(self):
        # dummy_desc = 'hello'*100
        return f"{self.name} type of {self.category} takes {self.prep_time}"
        #return f"{self.category}:{self.name}:{self.prep_time} min"


class Ingredient(models.Model):
    name = models.CharField(max_length=64,)
    price = models.DecimalField(max_digits=5, decimal_places=2) # max? 999.99
    recipes = models.ManyToManyField(Recipe, blank=True, related_name="ingredients")
    #non_optional_fun_name = models.CharField(max_length=64, default = None)

    def __str__(self):
        return f"{self.name} - ${self.price}"


    def ten_x_the_price(self):
        return self.price * 10


# class RecipeIngredient():
#     ingredient=FK
#     recipe=FK
#     relationship_nature = models.CharField(max_length=40)
