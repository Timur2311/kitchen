from import_export import resources
from recipe.models import Recipe, Ingredient

from recipe.helpers.functions import get_categories


class IngredientResource(resources.ModelResource):

    def skip_row(self, instance, original, row, import_validation_errors=None):
        if instance.name is None or not instance.name:
            return True
        return super().skip_row(instance, original, row,
                                import_validation_errors=import_validation_errors)

    def before_import_row(self, row, **kwargs):
        _ = get_categories(dict(row))
        row = dict(row)
        recipe_name = row["title"]
        if recipe_name is None:
            return super().before_import_row(row, **kwargs)

        recipe, _ = Recipe.objects.get_or_create(
            title=str(recipe_name), defaults={"title": recipe_name})

        # get hashtags and add to recipe
        hashtags = []
        for hashtag in row['hashtag'].split("#"):
            hashtags.append(hashtag)
        recipe.hashtags = hashtags

        # get steps and add to recipe
        steps = []
        for step in row['steps'].split("\n"):
            steps.append(step)
        recipe.steps = steps

        recipe.save()

        # get categories and add to recipe
        categories_list = get_categories(row)
        for category in categories_list:
            recipe.categories.add(category)

        # create ingredient objects
        for ingredient in row['ingredients'].split("\n"):
            name_quantity_list = None
            if "–" in ingredient:
                name_quantity_list = ingredient.split('–')
            elif "-" in ingredient:
                name_quantity_list = ingredient.split('-')
            if name_quantity_list is None:
                continue
            ings = Ingredient.objects.filter(recipe=recipe,
                                             name=name_quantity_list[0], quantity=name_quantity_list[1])
            ings_count = ings.count()
            if ings_count == 0:
                Ingredient.objects.create(
                    name=name_quantity_list[0], quantity=name_quantity_list[1], recipe=recipe)

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'qauntity', 'recipe')
