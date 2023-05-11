# Generated by Django 4.2 on 2023-05-11 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_rename_hashtag_recipe_hashtags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipe.recipe'),
        ),
    ]
