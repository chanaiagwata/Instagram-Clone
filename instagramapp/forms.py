from .models import Profile, Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile','likes','posted_at']
        
class DetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class authform(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')