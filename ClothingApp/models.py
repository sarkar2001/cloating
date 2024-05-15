from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    name = models.CharField(max_length=15)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name= "subcategory")


    def __str__(self):
        return self.name

class Subsubcategory(models.Model):
    name = models.CharField(max_length=15)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True,related_name= "subsubcategory")

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    size = models.CharField(max_length=200)

    def __str__(self):
        return self.size


class ProductColor(models.Model):
    color = models.CharField(max_length=200)

    def __str__(self):
        return self.color



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
        return self.title



class Variation(models.Model):
    sizetype = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    )
    range = (
        ('Black', 'Black'),
        ('Grey', 'Grey'),
        ('Green', 'Green'),
        ('White', 'White'),

    )
    product = models.ForeignKey(PRODUCT, on_delete=models.CASCADE)
    size = models.CharField(choices=sizetype,max_length=250,null=True,blank=True)
    color = models.CharField(choices=range,max_length=250,null=True,blank=True)
    stock = models.IntegerField(default=0,null=True)

    def is_out_of_stock(self):
        return self.stock <= 0

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(PRODUCT, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    variation = models.ForeignKey('Variation', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        size_display = self.variation.get_size_display() if self.variation else "N/A"
        color_display = self.variation.get_color_display() if self.variation else "N/A"
        return f"{self.user.username}'s Cart Item - Size: {size_display}, Color: {color_display}"



class BillingInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    def __str__(self):
        return self.firstname

class Order(models.Model):
    billinginfo = models.ForeignKey(BillingInfo, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=True, null=True, blank=True)
    status = models.CharField(max_length=100, default="pending")
    paymentSystem = models.CharField(max_length=100, default="Cash On Delivery")
    total = models.PositiveIntegerField(blank=True, null=True)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.billinginfo.firstname
