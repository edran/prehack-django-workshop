from django.conf.urls import patterns, url

urlpatterns = patterns('', 
    url(r'^albums/$', 'cdtracker.views.albums'),
    url(r'^artists/$', 'cdtracker.views.artists'),
    url(r'^album/(\d+)/$', 'cdtracker.views.albums'),
)