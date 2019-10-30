from django.shortcuts import render
from user_details import forms
from django.shortcuts import render
from user_details.forms import User_Form,User_Signup_Details
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
def home(request):
    return render(request,'user_details/success_signup.html')

def index(request):
    return render(request,'general_information/base.html')

def form_name_view(request):
    registered = False
    user_login_details = forms.User_Form()
    user_personal_details = forms.User_Signup_Details()
    if request.method == 'POST':
        form1 = forms.User_Form(request.POST)
        form2 = forms.User_Signup_Details(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.set_password(user.password)
            user.save()
            profile = form2.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            registered=True
            # login_credentials_instance = form1.save(commit=True)
            # user_details_instance = form2.save(commit=False)
            # user_details_instance.user_id = login_credentials_instance
            # user_details_instance.save()
            return home(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'user_details/registration.html',context={'user_login_details':user_login_details, 'user_personal_details':user_personal_details , 'registered': registered})
@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('general_information:home_page'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('general_information:home_page'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            return HttpResponse("invalid login details supplied!")
    else:
          return render(request,'user_details/login.html',{})
