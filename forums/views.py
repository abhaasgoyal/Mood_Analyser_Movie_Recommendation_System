from django.shortcuts import render
from .models import Post
from forums import forms
# Create your views here.
def home(request):
    return render(request,'forums/index.html')

def createpost(request):
    post_details = forms.User_Form()
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post=Post()
            post.title= request.POST.get('title')
            post.content= request.POST.get('content')
            post.save()

            return render(request, 'forums/index.html')
    return render(request,'forums/index.html', context = {'post_details' : post_details})
