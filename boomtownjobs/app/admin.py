from django.contrib import admin

from .models import *

class CompanyAdmin(admin.ModelAdmin):
    fields = ['company_name', 'location', 'skill']

class CandidateAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'location', 'skill']



admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Company, CompanyAdmin)


admin.site.register(Skill)
admin.site.register(Location)

