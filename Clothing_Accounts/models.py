from django.db import models


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