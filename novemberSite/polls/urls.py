from django.conf.urls import patterns, url, include

from polls import views

urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
    url(r'^more',views.anotherPage, name='anotherPage')
)