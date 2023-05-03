from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField


class Category(models.Model):
    title = models.CharField(max_length=32)
    subtitle = models.CharField(max_length=128)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title+" "+self.subtitle
    
class Ingredient(models.Model):
    name = models.CharField(max_length=8192)
    quantity = models.CharField(max_length = 128)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Recipe(models.Model):
    title = models.CharField(max_length = 16384)
    slug = models.SlugField(max_length=200)
    
    hashtag = ArrayField(models.CharField(max_length=8192))
    image = models.ImageField(upload_to= "recipe_photos/", blank=True, null=True)
    
    ingredients = models.ManyToManyField(Ingredient, related_name="recipes")
    steps = ArrayField(models.CharField(max_length=8192))
    
    
    categories = models.ManyToManyField(Category)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.slug
    
    
    
