from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=32)
    subtitle = models.CharField(max_length=128)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Recipe(models.Model):
    title = models.CharField(max_length = 16384)
    hashtag = models.CharField(max_length= 8192)
    image = models.ImageField(upload_to= "recipe_photos/")
    
    ingredianets = models.TextField()
    steps = models.TextField()
    
    category = models.ManyToManyField(Category)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
