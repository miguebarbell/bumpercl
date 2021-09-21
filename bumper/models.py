from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Product(models.Model):
    # name, price, description, date, available,
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=1000)
    stock = models.IntegerField()
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=False)
    CATEGORY_CHOICES = [('BIKE', 'Bikes'),
                        ('ROWER', 'Rowers'),
                        ('GENERAL', 'General Fitness'),
                        ('TREADMILL', 'Treadmills'),
                        ('BARBELL', 'Barbells'),
                        ('BUMPER', 'Bumpers')]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='GENERAL')

    def __str__(self):
        return self.name


class Order(models.Model):
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.id


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'%Y/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class MessageForm(models.Model):
    message = models.TextField(max_length=1000)
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=200, blank=True)
    phone = models.IntegerField(max_length=12, blank=True)
    date = models.DateTimeField(auto_now_add=True)
