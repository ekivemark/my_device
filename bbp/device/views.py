__author__ = 'mark'
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import Template, Context, RequestContext
from django.conf import settings as CONFIG
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView
import requests
import simplejson

@login_required()
def pipeline(request, *args, **kwargs ):

    call_to = CONFIG.VALIDIC_API +\
              "organizations/" \
              + CONFIG.V_ORG_ID + \
              ".json?access_token=" +\
              CONFIG.V_ACCESS_TOKEN

    print "call_to: %s" % call_to

    v = requests.get(call_to)
    print v.status_code
    print
    print "Returned: %s" % v.status_code
    vcontent = simplejson.loads(v.content)
    print vcontent
    vorg = vcontent['organization']
    p_status = 'CLOSED'
    if v.status_code == 200:

        print "Result:"
        print "working on it"
        print vorg['name']
        if vorg['name'] != "":
            p_status = 'OPEN'

    context = {'PAGE_TITLE': 'Device Pipeline Status',
               'ORG': vorg['name'],
               'P_STATUS': p_status,
               'ORG_USERS': vorg['users_provisioned'],}

    return render_to_response('device/pipeline.html', RequestContext(request, context))

def create_user(request, *args, **kwargs ):



    result = {'result':"none",'status': 200,}

    return(result)