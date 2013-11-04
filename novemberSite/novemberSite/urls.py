from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #ex: /polls/
    url(r'^polls/', include('polls.urls', namespace='polls')),
    #ex: /admin/
    url(r'^admin/', include(admin.site.urls)),
    #ex: /basketball/
    url(r'^basketball/', include('basketball.urls', namespace='basketball')),
    #ex: /trades/
    url(r'^trades/', include('trades.urls', namespace='trades')),
)
