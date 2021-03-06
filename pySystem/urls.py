from django.conf.urls import patterns, include, url
from django.contrib import admin
from sysadmin.views import current_datetime, login_index, register_index, register_new_user
# from logview.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pySystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', current_datetime ),
    #url(r'^$', login_index),
    url(r'^register/$', register_index ),
    url(r'^register/$', register_new_user),

    url(r'^$', 'logview.views.list_files'),
    url(r'^viewlog/(?P<sortmethod>.*?)/(?P<filename>.*?)/$','logview.views.view_log'),

)
