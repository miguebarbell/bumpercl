from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Email cannot be blank.")
        if not username:
            raise ValueError("Username cannot be blank.")
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email=self.normalize_email(email),
                                username=username,
                                password=password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)


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
                        ('BARBELL', 'Barbells'),
                        ('BUMPER', 'Bumpers')]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='GENERAL')

    def __str__(self):
        return self.name


class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    phone = models.CharField(max_length=12)
    bill_direction = models.CharField(max_length=500)
    ship_direction = models.CharField(max_length=500)
    cart = models.ManyToManyField(Product)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label):
        return True


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

    # def image_path(self):
    #     self.