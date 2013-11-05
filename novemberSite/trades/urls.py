from django.conf.urls import patterns, url
#from django.conf.urls import patterns, include, url

from trades import views
#from django.contrib import admin

#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<team_id>\d+)/team/$', views.team, name='team'),
    url(r'^tradeEnviro/$', views.tradeEnviro, name='tradeEnviro'),
    
    #url(r'^(?P<team_id>\d+)/$', views.team, name='team'),    #ex: /polls/4324    (?P<poll_id>\d+) --> poll_id='4324'
    #url(r'^(?P<team_id>\d+)/team/$', views.team, name='team'),  #ex: /polls/4324/results/
    #url(r'^(?P<team_id>\d+)/team/$', views.team, name='team'),    #ex: /polls/4324/vote/
    #url(r'^(?P<pk>\d+)/$', views.team, name='team'),    #ex: /polls/4324    (?P<poll_id>\d+) --> poll_id='4324'
    #url(r'^(?P<pk>\d+)/team/$', views.team, name='team'),  #ex: /polls/4324/results/
    #url(r'^(?P<pk>\d+)/team/$', views.team, name='team')    #ex: /polls/4324/vote/
)
