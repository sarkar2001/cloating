# Generated by Django 5.0.1 on 2024-03-29 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clothing_Accounts', '0007_alter_sliderbanner_sale_offer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='brand_logos/')),
            ],
        ),
    ]
