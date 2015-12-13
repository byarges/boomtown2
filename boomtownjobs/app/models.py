from django.db import models
from django import forms
from django.template.defaultfilters import slugify

class Skill(models.Model):
	skill = models.CharField(max_length=30)

	def __str__(self):             
		return self.skill



class Location(models.Model):
	state = models.CharField(max_length=30)

	def __str__(self):             
		return self.state

	

class Candidate(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	location = models.ForeignKey(Location)	
	skill = models.ForeignKey(Skill)
	
	def __str__(self):              
		return self.last_name + ', ' + self.first_name



class Company(models.Model):
	company_name = models.CharField(max_length=30)
	location = models.ForeignKey(Location)	
	skill = models.ForeignKey(Skill)

	def __str__(self):              
		return self.company_name
    
