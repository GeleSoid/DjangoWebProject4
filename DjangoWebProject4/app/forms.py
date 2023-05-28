"""
Definition of forms.
"""

from cProfile import label
from django.db import models
from.models import Comment
from .models import Blog

from dataclasses import fields
from email import message
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 

class AnketaForm(forms.Form):
    name = forms.CharField(label='Your name', min_length=2, max_length=100)
    city = forms.CharField(label='Your city', min_length=2, max_length=100)
    job = forms.CharField(label='Your occupation', min_length=2, max_length=100)
    gender = forms.ChoiceField(label='Your gender', 
                               choices=[('1', 'Man'), ('2', 'Woman')],
                               widget=forms.RadioSelect, initial=1)
    internet = forms.ChoiceField(label='Do you use the Internet', 
                               choices=(('1', 'Every day'),
                               ('2', 'Several times a day'),
                               ('3', 'Several times a week'),
                               ('4', 'Several times a month')), initial=1)
    notice = forms.BooleanField(label='Receive website news by e-mail?',
                                required=False)
    email = forms.EmailField(label='Yours by e-mail', min_length=7)
    message = forms.CharField(label='Briefly about yourself',
                              widget=forms.Textarea(attrs={'rows':12, 'cols':20}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Comment"}


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'image',)
        labels = {'title': "Title", 'description': "Description", 'content': "Content", 'image': "Image"}