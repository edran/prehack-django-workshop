from django.conf.urls import patterns, url

urlpatterns = patterns('', 
    url(r'^albumlist/$', 'cdtracker.views.albumlist'),
    url(r'^album/(\d+)/$', 'cdtracker.views.album'),
    url(r'^artistlist/$', 'cdtracker.views.artistlist'),
)