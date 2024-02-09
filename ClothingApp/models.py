from django.db import models
from autoslug import AutoSlugField
# Create your models here.


class CATEGORIES(models.Model):
    title = models.CharField(max_length=15)
    slug = AutoSlugField( populate_from='title',auto_created=True, unique=True)


    def __str__(self):
        return self.title


class PRODUCT(models.Model):
    CONDITION = (
        ('NEW', 'NEW'),
        ('OLD', 'OLD'),
    )
    title=  models.CharField(max_length=15)
    slug = AutoSlugField( populate_from='title',auto_created=True, unique=True)
    category= models.ForeignKey(CATEGORIES, on_delete=models.CASCADE, null=True, blank=True)
    image= models.ImageField(upload_to='PROD_PIC/')
    condition= models. CharField(choices=CONDITION, max_length=3)
    price= models.DecimalField(max_digits=7, decimal_places=2)
    description= models.TextField(max_length=250)

    def __str__(self):
        return self.title