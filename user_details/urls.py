from django.urls import path
from . import views
app_name = 'user_details'
urlpatterns = [
    path('', views.home, name = 'user_details'),
    path('registration', views.form_name_view, name='form_signup'),
    path('user_login', views.user_login, name='user_login')
]
