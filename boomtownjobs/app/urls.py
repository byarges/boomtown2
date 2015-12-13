from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^company/$', views.companypage, name='company'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^candidatepage/$', views.candidatepage, name='candidatepage'),
    # url(r'^candidate/(?P<pk>[0-9]+)/$', views.candidatequery, name='candidatequery'),
    
    url(r'^companyresults/$', views.companyresults, name='companyresults'),
    url(r'^companydetail/(?P<pk>[0-9]+)/$', views.companydetail, name='companydetail'),




    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
]