from django.shortcuts import render
from user_details import forms
from django.shortcuts import render
from django.http import HttpResponse
from user_details.forms import User_Signup,User_Signup_Details
def home(request):
    return render(request,'user_details/success_signup.html')

def form_name_view(request):
    user_login_details = forms.User_Signup()
    user_personal_details = forms.User_Signup_Details()
    if request.method == 'POST':
        form1 = forms.User_Signup(request.POST)
        form2 = forms.User_Signup_Details(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            login_credentials_instance = form1.save(commit=True)
            user_details_instance = form2.save(commit=False)
            user_details_instance.user_id = login_credentials_instance
            user_details_instance.save()
            return home(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'user_details/registration.html',context={'user_login_details':user_login_details, 'user_personal_details':user_personal_details })
