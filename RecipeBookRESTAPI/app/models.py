from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='Recipe')



    def __str__(self):
        return self.name


class Step(models.Model):
    step = models.TextField()
    recipe_step = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='Recipe_Step')


class Ingredient(models.Model):
    ingredient = models.TextField()
    recipe_ingredient = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='Recipe_Ingredient')
