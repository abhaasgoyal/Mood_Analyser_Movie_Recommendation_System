from django.shortcuts import render
from django.http import HttpResponse
from general_information.models import general_information
# Create your views here.
def home(request):
    webpages_list = general_information.objects.order_by('version_id')
    date_dict = { 'patch_notes': webpages_list}
    return render(request,'general_information/index.html', context=date_dict)
