from django.shortcuts import render
from .models import Product, ProductImage


# Create your views here.
def index(request):
    last_product = Product.objects.all().order_by('-date')[0]
    last_picture = ProductImage.objects.filter(product=last_product)
    # rowers = Product.objects.filter(category='ROWER')
    # barbells = Product.objects.filter(category='BARBELL')
    # bumpers = Product.objects.filter(category='BUMPER')
    # general = Product.objects.filter(category='GENERAL')
    return render(request, 'index.html', {'last': last_product, "last_picture": last_picture[0] })


def categories(request, category):
    items = Product.objects.filter(category=category)
    pictures = []
    for item in items:
        pictures.append(ProductImage.objects.filter(product=item))
    elements = zip(items, pictures)
    return render(request, 'categories.html', {'elements': elements, 'category': category})

