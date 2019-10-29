from django.shortcuts import render
from django.http import HttpResponse
from general_information.models import general_information
# Create your views here.
def general_info(request):
    webpages_list = general_information.objects.order_by('version_id')
    date_dict = { 'patch_notes': webpages_list}
    return render(request,'general_information/general_information.html', context=date_dict)

def home(request):
    return render(request,'general_information/base.html')
