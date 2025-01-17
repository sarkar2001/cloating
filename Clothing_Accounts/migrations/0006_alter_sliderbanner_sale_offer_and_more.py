# Generated by Django 5.0.1 on 2024-03-25 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clothing_Accounts', '0005_delete_hotdeal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderbanner',
            name='sale_offer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sliderbanner',
            name='starting_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sliderbanner',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
