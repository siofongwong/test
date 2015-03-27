from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^login/', 'sc1.views.login', name='login'),
    url(r'^home/', 'sc1.views.home', name='home'),
    url(r'^create_project/', 'sc1.views.create_project', name='create_project'),
    url(r'^project/(?P<title>\d{4})/$', 
        'sc1.views.project', name='project'),

    # private url
    url(r'^save_project/(?P<title>\w+)/(?P<git_link>\w+)/$', 
        'sc1.views.save_project', name='save_project'),

)
