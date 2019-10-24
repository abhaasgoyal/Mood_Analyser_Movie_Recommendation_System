from django import forms
from django.core import validators



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
