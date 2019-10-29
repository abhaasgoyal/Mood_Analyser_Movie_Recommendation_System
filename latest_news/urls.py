from django.urls import path
from . import views

app_name = 'latest_news'
urlpatterns = [
    path('', views.home, name = 'latest_news_home')
]
