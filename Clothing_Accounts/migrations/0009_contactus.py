# Generated by Django 5.0.1 on 2024-04-08 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clothing_Accounts', '0008_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, null=True)),
                ('address', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=20)),
                ('hotline', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('support_mail', models.EmailField(max_length=30)),
            ],
        ),
    ]
