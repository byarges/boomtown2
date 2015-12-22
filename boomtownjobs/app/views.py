from django.shortcuts import render, render_to_response, RequestContext
from django.shortcuts import get_object_or_404, render, redirect


from django.http import HttpResponse



from random import randrange
from .models import *
from django import forms
from django.db import models

from .forms import CompanyForm

import logging

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login


def index(request):
   
    return render(request, 'app/index.html')

def signin(request):
   
    return render(request, 'app/signin.html')

@login_required(login_url='/signin/')
def employerpage(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/companydetail/%d' % post.pk)
    else:
        form = CompanyForm()

    return render(request, 'app/employerpage.html', {'form': form})

@login_required(login_url='/signin/')
def candidatepage(request):

	
    state = Location.objects.all()
    skill = Skill.objects.all()

    return render_to_response ('app/candidatepage.html', {'states':state, 'skills':skill}, context_instance =  RequestContext(request),)  


def companyresults(request):

    state = request.GET.get("state_id")
    skill = request.GET.get("skill_id")



    try:

        query = Company.objects.filter(location__state__iexact=state).filter(skill__skill__iexact=skill)
    
    except(KeyError, Company.DoesNotExist):
        query = "No Matches"
    

    return render_to_response ('app/companyresults.html', {'query':query}, context_instance =  RequestContext(request))


def companydetail(request, pk):
    chosencompany = Company.objects.get(id=pk)

    return render_to_response ('app/companydetail.html', {'company':chosencompany})


# User Authentication
def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return render_to_response ('app/authtrue.html')
        else:
            # Return a 'disabled account' error message
            return render_to_response ('app/authenticate.html')
    else:
        # Return an 'invalid login' error message.
        return render_to_response ('app/authenticate.html')