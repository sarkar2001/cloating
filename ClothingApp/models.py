from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    name = models.CharField(max_length=15)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name

class Subsubcategory(models.Model):
    name = models.CharField(max_length=15)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class PRODUCT(models.Model):
    CONDITION = (
        ('NEW', 'NEW'),
        ('OLD', 'OLD'),
    )
    title=  models.CharField(max_length=15)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    subsubcategory = models.ForeignKey(Subsubcategory, on_delete=models.CASCADE, null=True, blank=True)
    image1= models.ImageField(upload_to='PRODUCT_PIC/',null=True)
    image2 = models.ImageField(upload_to='PRODUCT_PIC/', null=True,blank=True)
    image3 = models.ImageField(upload_to='PRODUCT_PIC/', null=True,blank=True)
    condition= models. CharField(choices=CONDITION, max_length=3)
    price= models.DecimalField(max_digits=7, decimal_places=2)
    description= models.TextField(max_length=250)
    is_hot_deal = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)

    def __str__(self):
        if hasattr(self, 'user'):
            return f"{self.user}'s {self.product_name}"  # Assuming user is the owner of the product
        else:
            return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(PRODUCT, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=5, blank=True, null=True)
    color = models.CharField(max_length=5, blank=True, null=True)


    def __str__(self):
        return self.user.username


class VariationManager(models.Manager):

    def sizes(self):
        return super(VariationManager, self).filter(variation='size')

    def colors(self):
        return super(VariationManager, self).filter(variation='color')



class Variation(models.Model):
    VARIATIONS_TYPE = (
        ('size', 'size'),
        ('color', 'color'),

    )

    product = models.ForeignKey(PRODUCT, on_delete=models.CASCADE)
    variation= models.CharField(choices=VARIATIONS_TYPE,max_length=20, null=True)
    name= models.CharField(max_length=20, null=True)
    stock = models.IntegerField(default=0)

    variation_obj= VariationManager()

    def is_out_of_stock(self):
        return self.stock <= 0