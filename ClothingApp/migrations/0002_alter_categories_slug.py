# Generated by Django 5.0.1 on 2024-02-01 06:05

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClothingApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]
