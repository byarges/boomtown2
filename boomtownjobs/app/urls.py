from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^candidatepage/$', views.candidatepage, name='candidatepage'),
    url(r'^employerpage/$', views.employerpage, name='employerpage'),    
    url(r'^companyresults/$', views.companyresults, name='companyresults'),
    url(r'^companydetail/(?P<pk>[0-9]+)/$', views.companydetail, name='companydetail'),
    url(r'^auth/$', views.auth, name='auth'),





]