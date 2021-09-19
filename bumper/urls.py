from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='indexbumper'),
    path('categoria/<str:category>', views.categories, name='categoriesbumper'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
