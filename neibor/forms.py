from django import forms
from .models import *

class BusinessesForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','location']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','location']

class UpdateProForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['name']

        