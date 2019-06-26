from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    # print("==================")
    # print("request is: ", request, "args is: ", args, "kwargs is: ", kwargs)
    # print("request user is : ", request.user)
    #return HttpResponse('<h1>Hello World</h1>')
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    #return HttpResponse('<h1>Welcome to the contact page</h1>')
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    #return HttpResponse('<h1>Welcome to the about page</h1>')
    return render(request, 'about.html', {})

def social_view(request, *args, **kwargs):
    #return HttpResponse('<h1>Welcome to the social page</h1>')
    return render(request, 'social.html', {})