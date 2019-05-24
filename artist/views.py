from django.views import generic
from django.shortcuts import render, render_to_response,  get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Artist, Catalogue, Bug, Feature, ArtForm
from django.utils import timezone #importing the timezone model
from datetime import datetime, timedelta # import to filter new recipes
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm #import to use the builtin user creation form

def index(request):
    
    context={
        'index': 'active'
    }
    return render(request, 'artist/index.html', context)

def start(request):
    
    context={
        'index': 'active'
    }
    return render(request, 'artist/start.html', context)


def catalogue(request):
    catalogues = Catalogue.objects.all()
    
    context={
        'object_list': catalogues,
        'catalogue': 'active'
    }
    return render(request, 'artist/catalogue.html',context)

def bug(request):
    bugs = Bug.objects.all()

    context={
        'bug': 'active'
    }
    return render(request, 'artist/bugs.html', context)

def feature(request):
    features = Feature.objects.all()
    
    context={
        'feature': 'active'
    }
    return render(request, 'artist/features.html', context)

def login(request):
    return render(request, 'registration/login.html',{})
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = UserCreationForm()
    context ={
        'form': form,
    }
    return render(request, 'registration/signup.html', context)