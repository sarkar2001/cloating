# Generated by Django 5.0.1 on 2024-03-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clothing_Accounts', '0006_alter_sliderbanner_sale_offer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderbanner',
            name='sale_offer',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sliderbanner',
            name='starting_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sliderbanner',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
