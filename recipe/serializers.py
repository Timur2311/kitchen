from rest_framework import serializers
from .models import Category, Recipe, Ingredient


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title' , 'subtitle' )
        
class IngredientSerializer(serializers.ModelSerializer):
    # recipe = serializers.PrimaryKeyRelatedField(read_only=True) 
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'quantity')
        
class RecipeSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    ingredients = IngredientSerializer(many=True, read_only = True)
    class Meta:
        model = Recipe
        fields = ('id', 'title' , 'slug' , 'hashtag', 'image', 'steps', 'category', "ingredients")
