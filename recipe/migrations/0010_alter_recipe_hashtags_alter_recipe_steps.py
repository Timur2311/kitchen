# Generated by Django 4.2 on 2023-05-16 12:03

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0009_alter_recipe_hashtags_alter_recipe_steps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='hashtags',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(blank=True, max_length=8192, null=True), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='steps',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(blank=True, max_length=8192, null=True), null=True, size=None),
        ),
    ]
