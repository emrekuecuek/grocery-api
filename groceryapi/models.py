from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    street_address = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    customer_id = models.IntegerField()


class TransactionStory(models.Model):
    customer_id = models.IntegerField()
    basket = models.CharField(max_length=250)
    purchase_count = models.IntegerField()


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    product_type = models.CharField(max_length=50)
    # TODO: add pictures

# Create your models here.
