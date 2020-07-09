from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, blank=True)
    name = models.CharField(null=True, max_length=50)
    email = models.EmailField(null=True, blank=True, max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(null=True, max_length=50)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(upload_to='images/', height_field=None,
                              width_field=None, max_length=None, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, blank=False, null=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now=False, auto_now_add=True)
    complete = models.BooleanField(default=False,  blank=False)
    transition_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.product.name

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, blank=False, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(null=True, blank=True, max_length=200)
    state = models.CharField(null=True, blank=True, max_length=200)
    city = models.CharField(null=True, blank=True, max_length=200)
    zip_code = models.CharField(null=True, blank=True, max_length=200)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.address