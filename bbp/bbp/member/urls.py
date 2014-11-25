__author__ = 'mark'
from django.conf.urls import patterns, url
"""
Validic Device Integration

"""

urlpatterns = patterns('',

    #CheckDevice Pipeline Status
    url(r'^view/$', 'bbp.member.views.view_member', name='member_view'),

)
