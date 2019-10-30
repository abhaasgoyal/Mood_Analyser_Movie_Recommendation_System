from django import forms
from django.core import validators
from user_details.models import User_Profile_Info
from django.contrib.auth.models import User
#if custom validation then specify the fields at '@'






class DateInput(forms.DateInput):
    input_type = 'date'

class User_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class User_Signup_Details(forms.ModelForm):

    class Meta:
        model = User_Profile_Info
        widgets = {
            'date_of_birth': DateInput()
        }
        exclude = ['user']


'''
def check_for_z(value):
    if value[0] == 'z':
        raise forms.ValidationError("z se start")
class FormName(forms.Form):
    user_id = forms.IntegerField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label= 'Enter Your email again:')
    password = forms.CharField()
    about = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:

            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")
'''
