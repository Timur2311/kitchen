# Generated by Django 4.2 on 2023-05-04 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_remove_recipe_ingredients_ingredient_recipe_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='categories',
        ),
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipe.category'),
            preserve_default=False,
        ),
    ]
