from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField

from helpers.models import BaseModel
from django.utils.text import slugify



class   Category(BaseModel):
    title = models.CharField(max_length=32)
    subtitle = models.CharField(max_length=128)

    def __str__(self):
        return self.title+" "+self.subtitle


class Recipe(BaseModel):
    title = models.CharField(max_length=16384)
    slug = models.SlugField(max_length=200)

    hashtags = ArrayField(models.CharField(max_length=8192, null=True, blank=True), default=list, null=True)
    image = models.ImageField(
        upload_to="recipe_photos/", blank=True, null=True)

    steps = ArrayField(models.CharField(max_length=8192, null=True, blank=True), default=list, null=True)

    categories = models.ManyToManyField(Category, related_name = "recipes")

    def __str__(self):
        return self.slug
    
    def save(self,*args,**kwargs):
        i = 1
        text = slugify(self.title)        
        while Recipe.objects.filter(slug = text).exists() :
            # avval tekstdan i ni olib tashlash kerak
            i+=1   
                     
            text = slugify(f"{text}+{i}")                           
        self.slug=slugify(text)        
        super(Recipe,self).save(*args,**kwargs)


class Ingredient(BaseModel):
    name = models.CharField(max_length=8192)
    quantity = models.CharField(max_length=128)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients", null = True, blank = True)
