from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^alertspusher/', include('alertspusher.c2dm.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login/'}),
    (r'^accounts/profile/$', 'alertspusher.c2dm.views.alert'),
)

urlpatterns += patterns('',
    (r'^assets/(?P<path>.*)$', 
    'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),    
)