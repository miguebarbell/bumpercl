from django.contrib import admin
from bumper.models import User, Product, Order, ProductImage
# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ProductImage)
