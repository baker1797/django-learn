from django.conf.urls import patterns, url
#from django.conf.urls import patterns, include, url

from trades import views
#from django.contrib import admin

#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^team/(?P<team_id>\d+)/$', views.team, name='team'),
    url(r'^tradeEnviro/$', views.tradeEnviro, name='tradeEnviro'),
    #url(r'^editPlayer/(?P<player_id>\d+)/$', views.editPlayer, name='editPlayer'),
    url(r'^editPlayer/$', views.editPlayer, name='editPlayer'),
)