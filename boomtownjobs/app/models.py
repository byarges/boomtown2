from django.db import models
from django import forms
from django.template.defaultfilters import slugify

from phonenumber_field.modelfields import PhoneNumberField


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
	phone_number = PhoneNumberField(default='+12069371234')
	nonvalidatedaddress = models.CharField(max_length=30, default='1234 99th Ave')
	email = models.EmailField(max_length=254, default='humanresources@fakeemail.com')
	description = models.CharField(max_length=450, default = '"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."')


	def __str__(self):              
		return self.company_name
    
