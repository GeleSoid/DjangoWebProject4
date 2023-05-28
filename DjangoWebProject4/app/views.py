"""
Definition of views.
"""

from datetime import date, datetime
from django.shortcuts import render, reverse, redirect
from django.http import HttpRequest
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from .forms import AnketaForm 

from django.db import models
from .models import Blog

from .models import Comment
from .forms import CommentForm, BlogForm


def home(request): 
    return render(request, 'app/index.html')

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request): 
    return render(request, 'app/about.html')

def sign_up(request):
    if request.method == 'POST':
        regform=UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()

            regform.save()

            return redirect('home')
    else:
        regform = UserCreationForm()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/signin.html',
        {
            'regform': regform,
            'year': datetime.now().year,
        }
    )


def get_absolute_url(self):
    return reverse('home', kwargs={'post_id': self.index})

def anketa(request):
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1': 'Man', '2': 'Women'}
    internet = {'1': 'Every day',
                '2': 'Several times a day',
                '3': 'Several times a week',
                '4': 'Several times a month'}
    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['city'] = form.cleaned_data['city']
            data['job'] = form.cleaned_data['job']
            data['gender'] = gender[ form.cleaned_data['gender'] ]
            data['internet'] = internet[ form.cleaned_data['internet'] ]
            if(form.cleaned_data['notice'] == True):
                data['notice'] = 'Yes'
            else:
                data['notice'] = 'No'
            data['email'] = form.cleaned_data['email']
            data['message'] = form.cleaned_data['message']
            form = None
    else:
        form = AnketaForm()
    return render(
        request,
            'app/anketa.html',
        {
            'form':form,
            'data':data
        }
    )

def blog(request):
    posts = Blog.objects.all()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title':'Blog',
            'posts': posts,
            'year':datetime.now().year,
        }
    )

def blogpost(request, parametr):
    assert isinstance(request, HttpRequest)
    post_1 = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parametr)
            comment_f.save()

            return redirect('blogpost', parametr=post_1.id)
    else:
        form = CommentForm()
    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1,
            'comments': comments,
            'form': form,
            'year': datetime.now().year,
        }
    )

def newpost(request):
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.autor = request.user
            blog_f.save()
            return redirect('blog')
    else:
        blogform = BlogForm()
    return render(
        request,
        'app/newpost.html',
        {
            'blogform': blogform,
            'title': 'Add a blog article',
            'year': datetime.now().year,
        }
    )

def videopost(request): 
    return render(request, 'app/videopost.html')