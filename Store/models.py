from django.db import models
from accounts.models import CustomUser
from django.utils.text import slugify
# Create your models here.


class Color(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True)
    stock = models.IntegerField(default=0)
    prod_img = models.ImageField(upload_to ="products", blank=True, null=True)
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    colors = models.ManyToManyField(Color, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

class Orderitems(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField( blank=True, null=True)

    def __str__(self):
        return f'{self.quantity} of {self.product}, ordered by {self.user.username}'
    
    def orderitem_price(self):
        return self.product.price * self.quantity

   


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    orderitems = models.ManyToManyField(Orderitems)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'cart of {self.user.username}'
    
    def cart_total_price(self):
        total = 0
        for orderitem in self.orderitems.all():
            total += orderitem.orderitem_price()
        return total

class VilleShipping(models.Model):
    name = models.CharField(max_length=128)
    price_shipping = models.FloatField(default=0.0)


class Filter(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=200, blank=True, null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Filter, self).save(*args, **kwargs)