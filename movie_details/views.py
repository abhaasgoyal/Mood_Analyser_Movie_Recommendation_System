from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,
                                  DetailView,CreateView,UpdateView,DeleteView)
from movie_details.models import movie_details
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h1>Movie Details</h1>')


class MovieListView(ListView):
    context_object_name = 'movies'
    model = movie_details
    template_name = 'movie_details/movies_list.html'

class MovieDetailView(DetailView):
    context_object_name = 'movies_detail'
    model = movie_details
    template_name = 'movie_details/movies_details.html'

class MovieNormalSearch(ListView):
    context_object_name = 'movies'
    model = movie_details.objects.order_by('movie_name')
    template_name = 'movie_details/movies_list.html'


class MovieMoodSearch(ListView):
    context_object_name = 'movies'
    model = movie_details
    template_name = 'movie_details/movies_list.html'
