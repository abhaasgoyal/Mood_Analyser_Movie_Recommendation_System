from django.shortcuts import render
from django.http import HttpResponse
from general_information.models import general_information
import requests
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import config
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
        config.r = requests.post('https://apikey:yTtyq_PBCWV83deTSX_mXhYGTPPisbwpxR6CVHX3nAhI@gateway-lon.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21', headers=headers, data=data)
        config.d = json.loads(config.r.text)
        print(config.d['document_tone']['tones'][0]['score'])
        print(config.d['document_tone']['tones'][0]['tone_id'])
        return HttpResponseRedirect(reverse('movie_details:movie_mood_search'))
    elif request.method =='POST' and request.POST.get('movie_search')!=None:
        config.search_string = request.POST.get('movie_search')
        return HttpResponseRedirect(reverse('movie_details:movie_normal_search'))
    return render(request,'general_information/base.html')
