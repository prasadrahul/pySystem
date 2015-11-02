from django.conf.urls import patterns, include, url
from django.contrib import admin
from sysadmin.views import current_datetime, login_index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pySystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', current_datetime ),
    url(r'^$', login_index),
)
