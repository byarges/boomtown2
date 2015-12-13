from django.shortcuts import render, render_to_response, RequestContext

from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render


from random import randrange
from .models import *
from django import forms
from django.db import models

import logging

def index(request):
   
    return render(request, 'app/index.html')

def signin(request):
   
    return render(request, 'app/signin.html')

def companypage(request):
    state = Location.objects.all()
    skill = Skill.objects.all()

    return render_to_response ('app/candidate.html', {'states':state, 'skills':skill}, context_instance =  RequestContext(request),)

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

