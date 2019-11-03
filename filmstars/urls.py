from django.urls import path
from django.urls import re_path
from . import views
app_name = 'filmstars'
urlpatterns = [
    path('',views.IndexView.as_view(),name='filmstars_home'),
    path('list', views.ActorListView.as_view(),name='filmstars_list'),
    re_path(r'^(?P<pk>[-\w]+)/$',views.ActorDetailView.as_view(),name='filmstars_details')
]
