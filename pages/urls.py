from django.urls import path
from . import views

# http://127.0.0.1:8000/

urlpatterns = [
    path('', views.index, name='index'), #kullanıcı boş bir link verdiğinde views altındaki index metodunu cagırıyoruz yani anasayfayı
    path('about', views.about, name='about'), #about viewvini çağırmak
]