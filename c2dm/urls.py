from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('alertspusher.c2dm.views',
    (r'^register/$', 'index'),
    (r'^register/(?P<device_id>[a-z0-9_]+)/$', 'register'),
    (r'^unregister/(?P<device_id>[a-z0-9_]+)/$', 'unregister'),
    (r'^alert/$', 'alert'),
    (r'^sendalert/$', 'sendAlert')
)