from django.shortcuts import render
from user_details import forms
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'user_details/success_signup.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING HERE
            print("VALIDATION SUCCESS!")
            print(form.cleaned_data['user_id'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['password'])
            print(form.cleaned_data['about'])


    return render(request,'user_details/registration.html',{'form':form})
