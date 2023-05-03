from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from .models import Recipe, Category, Ingredient

admin.site.register(Ingredient)
admin.site.register(Category)
class RecipeAdmin(admin.ModelAdmin,DynamicArrayMixin):
    list_display = ('id', 'title' , 'slug' , 'hashtag', 'image',  'steps', )
    
admin.site.register(Recipe, RecipeAdmin)