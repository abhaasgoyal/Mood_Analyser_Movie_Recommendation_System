from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,
                                  DetailView,CreateView,UpdateView,DeleteView)
from movie_details.models import movie_details
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import datetime
import configformovies

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
        try:
            ctx = super(MovieNormalSearch, self).get_context_data(**kwargs)
            ctx['movies'] = movie_details.objects.filter(movie_name__icontains = configformovies.search_string).values('movie_name','movie_id')
            return ctx
        except:
            print("error.. go to home page and try again!")

class MovieMoodSearch(ListView):
    template_name = 'movie_details/movies_list.html'

    #start


    #end
    def get_queryset(self):
        return movie_details.objects.all()

    def get_context_data(self, **kwargs):

        ctx = super(MovieMoodSearch, self).get_context_data(**kwargs)
        x= movie_details.objects.values('genre','movie_name','movie_id')
        list = []
        if configformovies.search_mood_score > 0.5:
            dict ={"anger": "War" if configformovies.search_mood_score > 0.72 else "Action",
                    "fear": "Thriller" if configformovies.search_mood_score > 0.67 else "Drama",
                    "analytical": "History" if configformovies.search_mood_score > 0.78 else "Sci-Fi",
                    "joy": "Romance" if configformovies.search_mood_score > 0.75 else "Fantasy",
                    "sadness": "Drama" if configformovies.search_mood_score > 0.65 else "Crime",
                    "confident": "Biography" if configformovies.search_mood_score > 0.70 else "Adventure",
                    "tentative": "Western"
                    }
            for share in x:
                genre_list = share['genre'].replace(" ","").split(',')
                #here genre is being split
                predicted_genre = dict[configformovies.search_mood_mood]
                if predicted_genre in genre_list:
                    list.append(share)

        ctx['movies'] = list
        return ctx
