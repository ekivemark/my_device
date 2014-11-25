from django.conf.urls import patterns, url
__author__ = 'mark'
"""
Validic Device Integration

"""

urlpatterns = patterns('',

    #CheckDevice Pipeline Status
    url(r'^status/$', 'device.views.pipeline', name='status'),
    url(r'^create_user/$', 'device.views.create_user'),

)
