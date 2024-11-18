from django.shortcuts import render

from django.template import loader

from django.http import HttpResponse

# Create your views here.

def signup(request):
    signUpTemplate = loader.get_template('signup.html')

    return HttpResponse( signUpTemplate.render() )

def signin(request):
    signInTemplate = loader.get_template('signin.html')

    return HttpResponse( signInTemplate.render() )

