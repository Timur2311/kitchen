
from ..models import Category


def get_categories(row):
   
    categories = []
    if row['category_subtitle'] is not None:
        cat_subtitle_list = row['category_subtitle'].split('\n')
        for cat_index, cat_title in enumerate(row['category_title'].split("\n")):
            category = None
            cats = Category.objects.filter(
                title=cat_title, subtitle=cat_subtitle_list[cat_index])
            cats_count = cats.count()
            if cats_count == 0:
                category, _ = Category.objects.get_or_create(
                    title=cat_title, subtitle=cat_subtitle_list[cat_index], defaults={'title': cat_title, 'subtitle': cat_subtitle_list[cat_index]})
            else:
                category = cats[0]
            categories.append(category)
        return categories
    return None
