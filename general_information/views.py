from django.shortcuts import render
from django.http import HttpResponse
from general_information.models import general_information
import requests
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import configformovies
# Create your views here.
def general_info(request):
    webpages_list = general_information.objects.order_by('version_id')
    date_dict = { 'patch_notes': webpages_list}
    return render(request,'general_information/general_information.html', context=date_dict)

def home(request):
    if request.method == 'POST' and request.POST.get('mood')!=None:
        mood = request.POST.get('mood')
        headers = {'Content-Type': 'application/json'}
        data = bytes('{\"text\":\"'+mood+'\"}', 'utf-8')
        configformovies.r = requests.post('https://apikey:yTtyq_PBCWV83deTSX_mXhYGTPPisbwpxR6CVHX3nAhI@gateway-lon.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21', headers=headers, data=data)
        configformovies.d = json.loads(configformovies.r.text)
        print(configformovies.d['document_tone']['tones'][0]['score'])
        print(configformovies.d['document_tone']['tones'][0]['tone_id'])
        configformovies.search_mood_score = configformovies.d['document_tone']['tones'][0]['score']
        configformovies.search_mood_mood = configformovies.d['document_tone']['tones'][0]['tone_id']

        return HttpResponseRedirect(reverse('movie_details:movie_mood_search'))
    elif request.method =='POST' and request.POST.get('movie_search')!=None:
        configformovies.search_string = request.POST.get('movie_search')
        return HttpResponseRedirect(reverse('movie_details:movie_normal_search'))
    return render(request,'general_information/base.html')
