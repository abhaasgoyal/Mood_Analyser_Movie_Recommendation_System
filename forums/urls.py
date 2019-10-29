from django.urls import path
from . import views
app_name= 'forums'
urlpatterns = [
    path('', views.home, name = 'forums_home')
]
