
# import form class from django
from django import forms
from django.contrib.auth.forms import UserCreationForm

# import GeeksModel from models.py
from .models import Community, User, Post
  
# create a ModelForm
class CommForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Community
        fields = "__all__"
        
class RegisterForm(UserCreationForm):

    class Meta:
	    model = User
	    fields = '__all__'
	    
	    
class PostForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Post
        fields = ['text','image']
        
