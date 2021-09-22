from django.shortcuts import render
from .models import Product, ProductImage, Notice


# Create your views here.
def index(request):
    last_product = Product.objects.all().order_by('-date')[0]
    last_picture = ProductImage.objects.filter(product=last_product)
    try:
        print('Getting last notice')
        last_notice = Notice.objects.filter(active_notice=True)[0]
        return render(request, 'index.html',
                      {'last': last_product, "last_picture": last_picture[0], 'last_notice': last_notice})
    except IndexError:
        print('No defined a last notice.')
    return render(request, 'index.html', {'last': last_product, "last_picture": last_picture[0]})


def categories(request, category):
    items = Product.objects.filter(category=category)
    pictures = []
    for item in items:
        pictures.append(ProductImage.objects.filter(product=item))
    elements = zip(items, pictures)
    return render(request, 'categories.html', {'elements': elements, 'category': category})


