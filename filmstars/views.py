from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,
                                  DetailView,CreateView,UpdateView,DeleteView)
from django.http import HttpResponse
from . import models
# class home(View):
#     def get(self,request):
#         return HttpResponse('filmstars are cool')
#
#

class IndexView(TemplateView):
    template_name= 'index.html'

class ActorListView(ListView):
    context_object_name = 'filmstars'
    model = models.filmstars
    template_name = 'filmstars/filmstar_list.html'

class ActorDetailView(DetailView):
    context_object_name = 'filmstars_detail'
    model = models.filmstars
    template_name = 'filmstars/filmstar_details.html'
