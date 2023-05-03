from rest_framework import serializers
from recipe.models import Category, Recipe


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title' , 'subtitle' )
        
class RecipeSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Recipe
        fields = ('id', 'title' , 'slug' , 'hashtag', 'image', 'ingredients', 'steps', 'categories')
