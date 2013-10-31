from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
    url(r'^more/$',views.anotherPage, name='anotherPage'),
    #ex: /polls/4324
    # (?P<poll_id>\d+) --> poll_id='4324'
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    #ex: /polls/4324/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    #ex: /polls/4324/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote')
)