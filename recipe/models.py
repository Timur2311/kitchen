from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=32)
    subtitle = models.CharField(max_length=128)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title+" "+self.subtitle
    
class Recipe(models.Model):
    title = models.CharField(max_length = 16384)
    slug = models.SlugField(max_length=200)
    
    hashtag = models.CharField(max_length= 8192)
    image = models.ImageField(upload_to= "recipe_photos/")
    
    ingredients = models.TextField()
    steps = models.TextField()
    
    categories = models.ManyToManyField(Category)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.slug
    
    
    
