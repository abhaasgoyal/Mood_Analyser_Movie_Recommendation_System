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
    template_name= 'filmstars/filmstar_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Welcome to actors!'
        return context

class ActorListView(ListView):
    context_object_name = 'filmstars'
    model = models.filmstars
    template_name = 'filmstars/filmstars_list.html'

class ActorDetailView(DetailView):
    context_object_name = 'filmstars_detail'
    model = models.filmstars
    template_name = 'filmstars/filmstars_details.html'
