# Generated by Django 5.0.1 on 2024-02-01 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClothingApp', '0002_alter_categories_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(auto_created=True, unique=True),
        ),
    ]