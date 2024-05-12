from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class SliderBanner(models.Model):
    image = models.ImageField(upload_to='slider/')
    sale_offer = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title




class AboutUs(models.Model):
    title = models.CharField(max_length=50,null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='aboutimage/',null=True)


    def __str__(self):
        return self.title


class Brand(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='brand_logos/')

    def __str__(self):
        return self.name



class ContactUs(models.Model):
    title = models.CharField(max_length=500, null=True)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    hotline = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    support_mail = models.EmailField(max_length=30)

    def __str__(self):
        return f"{self.email}"

class UserMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"