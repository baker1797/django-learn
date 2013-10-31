from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    #url(r'^more/$',views.anotherPage, name='anotherPage'),
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),    #ex: /polls/4324    (?P<poll_id>\d+) --> poll_id='4324'
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),  #ex: /polls/4324/results/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote')    #ex: /polls/4324/vote/
)