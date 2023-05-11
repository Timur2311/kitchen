from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


from .models import Recipe, Category, Ingredient

# from .model_resouce import RecipeResource
from import_export.admin import ImportExportModelAdmin, ImportExportMixin, ExportActionMixin, ImportMixin

admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Recipe)


# @admin.register(Recipe)
# class RecipeAdmin(ImportExportModelAdmin,admin.ModelAdmin,DynamicArrayMixin):
#     class Meta:
#         resource_class = RecipeResource
        
   
    
