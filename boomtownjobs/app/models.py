from django.db import models
from django import forms

class Skill(models.Model):
	skill = models.CharField(max_length=30)

	def __str__(self):              # __unicode__ on Python 2
		return self.skill



class Location(models.Model):
	state = models.CharField(max_length=30)

	def __str__(self):              # __unicode__ on Python 2
		return self.state

	

class Candidate(models.Model):
	#candidate_id here ???
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	location = models.ForeignKey(Location)	
	#birthdate = DateField(auto_now=False, auto_now_add=False)
	skill = models.ForeignKey(Skill)
	

	def __str__(self):              # __unicode__ on Python 2
		return self.last_name + ', ' + self.first_name

	#phone stuff
	#phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #phone_number = models.CharField(validators=[phone_regex], blank=True) # validators should be a list


    

    


class Company(models.Model):
	#Company_id here ???
	company_name = models.CharField(max_length=30)
	location = models.ForeignKey(Location)	
	skill = models.ForeignKey(Skill)	
	#phone stuff
	#phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #phone_number = models.CharField(validators=[phone_regex], blank=True) # validators should be a list
	def __str__(self):              # __unicode__ on Python 2
		return self.company_name
    



