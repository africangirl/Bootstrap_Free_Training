from django import forms
from .models import Post
from .models import Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'Type', 'created_at']


class ProfileForm(forms.ModelForm):
    class Meta: #Used to define some attributes
        model = Profile
        fields = ['bio', 'location', 'profile_pic']