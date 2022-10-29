from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

## dummy dataset
posts = [
    {
        'author': 'test1',
        'title': 'test Blog',
        'content': 'test 1 with dummy data',
        'date_posted': 'August 23, 2022'
    },
    {
        'author': 'test2',
        'title': 'test Blog 2',
        'content': 'test 2 with dummy data',
        'date_posted': 'August 24, 2022'
    },
]


def home(request):
    context = {
        ## Post.objects.all()
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})