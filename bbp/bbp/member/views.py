__author__ = 'mark'
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import Template, Context, RequestContext
from django.conf import settings as CONFIG
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView

from models import Member

@login_required()
def view_member(request):
    u = User(username=request.user)
    m = Member(member=request.user)
    print "User: %s" % u.username

    print "Member: %s" % (m.member)

    context = {'PAGE_TITLE': 'Member Profile',
               'MEMBER': m,
                'USER': u,}
    return render_to_response('member/profile.html', RequestContext(request, context))
