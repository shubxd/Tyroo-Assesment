from django.db import models

# Create your models here.

class Categories(models.Model):
    PRODUCT_TYPES = (
        (1, "ELECTRONICS"),
        (2, "SPORTS"),
        (3, "GROCERIES"),
        (4, "TOILETRIES"),
        (5, "CLOTHING"),
    )
    name = models.CharField(max_length=100, unique=True)
    type = models.IntegerField(choices=PRODUCT_TYPES)

class Brand(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand  = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField(null=True)
    type = models.ForeignKey(Categories, on_delete=models.CASCADE)
    stock = models.IntegerField(default=100)
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

