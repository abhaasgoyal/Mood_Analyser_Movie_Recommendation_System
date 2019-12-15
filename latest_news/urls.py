from django.urls import path
from . import views

app_name = 'latest_news'
urlpatterns = [
    path('', views.home, name = 'latest_news_home'),
    path('aamir.html', views.aamir, name = ''),
    path('amitabh.html', views.amitabh, name = ''),
    path('naseer.html', views.naseer, name = ''),
    path('shahrukh.html', views.shahrukh, name = ''),
    path('salman.html', views.salman, name = ''),
    path('sanjay.html', views.sanjay, name = ''),
    path('akshay.html', views.akshay, name = ''),
    path('pacino.html', views.pacino, name = ''),
    path('bale.html', views.bale, name = ''),
    path('phoenix.html', views.phoenix, name = ''),
]
