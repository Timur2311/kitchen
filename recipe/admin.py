from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


from .models import Recipe, Category, Ingredient

from .resource import IngredientResource
from import_export.admin import ImportExportModelAdmin, ImportMixin


admin.site.register(Ingredient)
admin.site.register(Category)


@admin.register(Recipe)
class RecipeAdmin(ImportExportModelAdmin, ImportMixin, DynamicArrayMixin):

    resource_classes = [IngredientResource]
