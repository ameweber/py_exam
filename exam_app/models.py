import uuid
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class User(models.Model):
    email = models.CharField(max_length=150)
    fullname = models.CharField(max_length=150)
    password = models.CharField(max_length=150)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='products')

    def __str__(self):
        return self.name


class ProductVersion(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    product = models.ForeignKey(Product, related_name='product_versions')
    # stock = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey('auth.User')
    shipping_address = models.TextField()
    shipping_date = models.DateTimeField(auto_now=False)
    product = models.ForeignKey(Product, related_name='orders')

    def __str__(self):
        result = self.product + self.user
        return result