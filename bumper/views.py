from django.shortcuts import render
from .models import Product, ProductImage


# Create your views here.
def index(request):
    # retrieve for category
    # CATEGORY_CHOICES = [('BIKE', 'Bikes'), ('GENERAL', 'General Fitness')]
    bikes = Product.objects.filter(category='BIKE')
    last_bike = Product.objects.all().order_by('-date')[0]
    last_bike_picture = ProductImage.objects.all().order_by('-date')[0]
    # last_bike_picture = ProductImage.objects.filter(product=last_bike)
    rowers = Product.objects.filter(category='ROWER')

    barbells = Product.objects.filter(category='BARBELL')
    bumpers = Product.objects.filter(category='BUMPER')
    general = Product.objects.filter(category='GENERAL')
    print(bikes)
    print(last_bike)
    print(type(last_bike))
    print(last_bike_picture)
    print(last_bike.name)
    # print(last_bike_picture.date)
    return render(request, 'index.html', { 'last_bike': last_bike, "last_bike_picture": last_bike_picture })
