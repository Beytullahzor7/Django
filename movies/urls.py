from django.urls import path
from . import views

#127.0.0.1:8000/movies
#127.0.0.1:8000/movies/2        #2 numaralı id ye sahip movie bilgisini almak istersek
#127.0.0.1:8000/movies/search

urlpatterns = [
    path('', views.index, name='movies'), #boş '' movies sayfasını simgeler

    path('<int:movie_id>', views.detail, name='detail'),

    path('search', views.search, name='search'),
]