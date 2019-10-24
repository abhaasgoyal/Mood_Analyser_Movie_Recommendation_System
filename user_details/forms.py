from django import forms
from django.core import validators
from user_details.models import login_credentials
#if custom validation then specify the fields at '@'















class User_Signup(forms.ModelForm):
    #'@'
    class Meta:
        model = login_credentials
        #option 1 is always fields = "_all"
        #option 2 is exclude exclude = ["field1","field2"]
        #option 3 is include fields = ("field1","field2")
        fields = "__all__"

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
