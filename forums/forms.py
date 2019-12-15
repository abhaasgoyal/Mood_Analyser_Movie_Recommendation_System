from django import forms
from forums.models import Post
#if custom validation then specify the fields at '@'

class User_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content')
