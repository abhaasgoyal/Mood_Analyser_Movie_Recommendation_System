from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'user_details'),
    path('registration', views.form_name_view, name='form_signup'),
]
