__author__ = 'mark'
from django.conf.urls import patterns, url
from vutils import get_organization, full_server_address
"""
Validic Device Integration

"""

urlpatterns = patterns('',

    #CheckDevice Pipeline Status
    url(r'^view/$', 'bbp.member.views.view_member', name='member_view'),
    url(r'^get_id/$', 'bbp.member.views.get_ext_id', name='member_get_id'),
    url(r'^full_server_address/$', 'bbp.member.vutils.full_server_address', name="validic_server_address"),


)
