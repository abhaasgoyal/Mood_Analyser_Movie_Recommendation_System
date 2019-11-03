from django.urls import path, re_path
from . import views
from .models import movie_details
import datetime
app_name = 'movie_details'
urlpatterns = [
    path('list', views.MovieListView.as_view(),name='movies_list'),
    path('mood_search', views.MovieMoodSearch.as_view(),name='movie_mood_search'),
    path('normal_search',views.MovieNormalSearch.as_view(),name='movie_normal_search'),
    re_path(r'^(?P<pk>[-\w]+)/$',views.MovieDetailView.as_view(),name='movies_details'),

]
