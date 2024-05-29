from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_product_list(self):
        return PRODUCT.objects.filter(
            product_category__subcategory__category=self,
        )

class SubCategory(models.Model):
    name = models.CharField(max_length=15)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=15)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    size = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.size


class ProductColor(models.Model):
    color = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.color



class PRODUCT(models.Model):
    CONDITION = (
        ('NEW', 'NEW'),
        ('OLD', 'OLD'),
    )
    title=  models.CharField(max_length=50)
    # category= models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    # subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True)
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

class ProductSizeThrough(models.Model):
    product = models.ForeignKey(PRODUCT, on_delete=models.CASCADE)
    product_size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.title} - {self.product_size.size}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(PRODUCT, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.ForeignKey(ProductSizeThrough, on_delete=models.CASCADE, blank=True, null=True)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        size_display = self.size.product_size.size if self.size else "N/A"
        return f"{self.user.username}'s Cart Item - Product: {self.product.title}, Size: {size_display}"
    
    def subtotal(self):
        if self.product.price:
            return self.product.price * self.quantity
        else:
            return 0  # Or handle the case where price is not available


class DeliveryAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    PAYMENTSYSTEM = [
        ("COD", "cash_on_delivery"),
        # ("SSL", "ssl_commerz"),
    ]
    order_item = models.ManyToManyField(Cart, related_name="order_item")
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now=False, auto_now_add=True, null=True, blank=True)
    paymentSystem = models.CharField(choices=PAYMENTSYSTEM, max_length=250, null=True, blank=True)
    delivery_fee = models.PositiveIntegerField(null=True, blank=True)
    total = models.PositiveIntegerField(blank=True, null=True)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
