from django.contrib.auth.models import  User
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name 

class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name 



class Product(models.Model):
    CATEGORY = (
                ('indoor', 'indoor'),
                ('out door ', 'out door'),
                ('both door', 'both door')
              )

    name= models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    description = models.TextField(blank=True)
    product_pic = models.ImageField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name 




class Order(models.Model):
    STATUS = (
                ('pending', 'pending'),
                ('out for delivery', 'out for delivery'),
                ('Delivered', 'Delivered')
              )
    pass
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=200, null=True,)

    def __str__(self):
        return self.product.name  

    