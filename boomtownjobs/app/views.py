from django.shortcuts import render, render_to_response, RequestContext

from django.http import HttpResponse

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
    # form = request.POST
    
    # if request.method == 'POST':
    #   selected_item = get_object_or_404(Item, pk=request.POST.get('item_id'))
    #   # get the user you want (connect for example) in the var "user"
    #   # item = selected_item
    #   # save()
    return render_to_response ('app/test.html', {'states':state, 'skills':skill}, context_instance =  RequestContext(request),)  

    # return render(request, 'app/test.html')



def candidatequery(request, pk):
    query = Company.objects.filter(location__state__iexact='WA').filter(skill__skill__iexact='Concrete')


    return render_to_response ('app/test2.html', {'query':query}, context_instance =  RequestContext(request))

def catchparams(request):

    state = request.GET.get("state_id")
    skill = request.GET.get("skill_id")


    try:

        query = Company.objects.filter(location__state__iexact=state).filter(skill__skill__iexact=skill).values_list('company_name', flat=True)
       
    
    except(KeyError, Company.DoesNotExist):
        query = "No Matches"
    

    return render_to_response ('app/test2.html', {'query':query}, context_instance =  RequestContext(request))


