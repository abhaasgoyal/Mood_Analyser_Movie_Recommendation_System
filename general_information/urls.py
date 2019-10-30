from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'general_information'
urlpatterns = [
    path('general_information', views.general_info, name = 'general_information_home'),
    path('', views.home, name = 'home_page'),
]
