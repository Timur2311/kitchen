from rest_framework import generics

from recipe import models, serializers


class RecipeCategoryListAPIView(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    pagination_class = None


class RecipeListListAPIView(generics.ListAPIView):
    serializer_class = serializers.RecipeSerializer
    queryset = models.Recipe.objects.all().prefetch_related('categories')
    filterset_fields = {'categories': {'in'}}


class RecipeListDetailAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.RecipeSerializer
    queryset = models.Recipe.objects.all().prefetch_related('categories')
