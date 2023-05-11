# from recipe.models import Recipe, Category
# from . import serializers
# from rest_framework import generics

# from django_filters.rest_framework import DjangoFilterBackend


# class RecipeList(generics.ListAPIView):
#     serializer_class = serializers.RecipeSerializer
#     queryset = Recipe.objects.all()
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ('category',)


# class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = serializers.RecipeSerializer
#     lookup_field = "slug"


# class CategoryList(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = serializers.CategorySerializer

from .models import Category, Ingredient, Recipe
from django.http import HttpResponse

import pandas as pd


def saving_data(request):
    workbook = pd.read_excel(f'recipe/recipes.xlsx')

    # extracting data from excel adn converting it to list
    recipes_titles_list = workbook['title'].tolist()
    recipes_hashtags_list = workbook['hashtag'].tolist()
    cat_title_list = workbook['category_title'].tolist()
    cat_subtitle_list = workbook['category_subtitle'].tolist()
    ingredients_list = workbook['ingredients'] .tolist()
    steps_list = workbook['steps'].tolist()
    
    steps = []
    hashtags = []

    # loop all recipes from file
    for recipe_index in range(len(recipes_titles_list)):

        # get recipe title
        title = recipes_titles_list[recipe_index]

        # get recipe hashtags
        for hashtag in recipes_hashtags_list[recipe_index].split("#"):
            hashtags.append(hashtag)

        # get recipe steps
        for step in steps_list[recipe_index].split("\n"):
            steps.append(step)
            
        # create recipe object
        recipe = Recipe.objects.create(
            title=title, hashtags=hashtags, steps=steps)

        # get recipe ingredients
        name_quantity_list = ingredients_list[recipe_index].split("–")
        name_quantity_list_length = len(name_quantity_list)
        print(f"\n\nlist --- {name_quantity_list}\n\n")
        for index in range(name_quantity_list_length):
            print("\n\n for ga kirdi\n\n")
            if index == name_quantity_list_length-1:
                print("\n\nbreak\n\n")
                break
            ings = Ingredient.objects.filter(recipe = recipe,
                name=name_quantity_list[index], quantity=name_quantity_list[index+1])
            ings_count = ings.count()
            if ings_count == 0 and index % 2 == 0:
                print("\n\nif ga kirdi\n\n")
                Ingredient.objects.create(
                    name=name_quantity_list[index], quantity=name_quantity_list[index+1], recipe=recipe)
            


    
        # get recipe categories and add to recipe
        for cat_index, cat_title in enumerate(cat_title_list[recipe_index].split("\n")):
            category = None
            cats = Category.objects.filter(
                title=cat_title, subtitle=cat_subtitle_list[recipe_index].split("\n")[cat_index])
            cats_count = cats.count()
            if cats_count == 0:
                category = Category.objects.create(
                    title=cat_title, subtitle=cat_subtitle_list[recipe_index].split("\n")[cat_index])
            else:
                category = cats[0]

            recipe.categories.add(category)
    html = "<html><body>It is now success.</body></html>" 
    return HttpResponse(html)
    