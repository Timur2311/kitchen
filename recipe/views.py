from recipe.models import Recipe, Category
from . import serializers
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend

class RecipeList(generics.ListAPIView):
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('category',)
    

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
    lookup_field = "slug"
    
    


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    
    