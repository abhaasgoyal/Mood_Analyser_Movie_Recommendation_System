from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,
                                  DetailView,CreateView,UpdateView,DeleteView)
from movie_details.models import movie_details
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import datetime
import config
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
    template_name = 'movie_details/movies_list.html'
    def get_queryset(self):
        return movie_details.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super(MovieNormalSearch, self).get_context_data(**kwargs)
        ctx['movies'] = movie_details.objects.filter(movie_name__icontains = config.search_string).values('movie_name','movie_id')
        return ctx

class MovieMoodSearch(ListView):

    context_object_name = 'movies'
    model = movie_details
    template_name = 'movie_details/movies_list.html'
