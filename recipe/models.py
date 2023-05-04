from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField

from helpers.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=32)
    subtitle = models.CharField(max_length=128)

    def __str__(self):
        return self.title+" "+self.subtitle


class Recipe(BaseModel):
    title = models.CharField(max_length=16384)
    slug = models.SlugField(max_length=200)

    hashtag = ArrayField(models.CharField(max_length=8192))
    image = models.ImageField(
        upload_to="recipe_photos/", blank=True, null=True)

    steps = ArrayField(models.CharField(max_length=8192))

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.slug


class Ingredient(BaseModel):
    name = models.CharField(max_length=8192)
    quantity = models.CharField(max_length=128)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients")
