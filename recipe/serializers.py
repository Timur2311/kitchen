from rest_framework import serializers
from recipe import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'title', 'subtitle')


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ingredient
        fields = ('name', 'quantity')


class RecipeSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many = True)
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = models.Recipe
        fields = ('id', 'title', 'slug', 'hashtags', 'image',
                  'steps', 'categories', "ingredients")
