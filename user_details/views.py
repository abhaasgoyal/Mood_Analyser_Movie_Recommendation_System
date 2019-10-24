from django.shortcuts import render
from user_details import forms
from django.shortcuts import render
from django.http import HttpResponse
from user_details.forms import User_Signup
def home(request):
    return render(request,'user_details/success_signup.html')

def form_name_view(request):
    form = forms.User_Signup()

    if request.method == 'POST':
        form = forms.User_Signup(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)

        else:
            print('ERROR FORM INVALID')

    return render(request,'user_details/success_signup.html')
