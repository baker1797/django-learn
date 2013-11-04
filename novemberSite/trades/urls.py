from django.conf.urls import patterns, url
#from django.conf.urls import patterns, include, url

from trades import views
#from django.contrib import admin

#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<team_id>\d+)/$', views.team, name='team'),
)
