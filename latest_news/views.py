from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'latest_news/index.html')
def aamir(request):
    return render(request,'latest_news/aamir.html')
def amitabh(request):
    return render(request,'latest_news/amitabh.html')
def naseer(request):
    return render(request,'latest_news/naseer.html')
def shahrukh(request):
    return render(request,'latest_news/shahrukh.html')
def salman(request):
    return render(request,'latest_news/salman.html')
def sanjay(request):
    return render(request,'latest_news/sanjay.html')
def akshay(request):
    return render(request,'latest_news/akshay.html')
def pacino(request):
    return render(request,'latest_news/pacino.html')
def bale(request):
    return render(request,'latest_news/bale.html')
def phoenix(request):
    return render(request,'latest_news/phoenix.html')
