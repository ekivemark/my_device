__author__ = 'mark'
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import Template, Context, RequestContext
from django.conf import settings as CONFIG
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView

from vutils import full_server_address, get_marketplace, get_organization, marketplace_auth
import urllib
import httplib
import json
import requests


from django.http import JsonResponse

from models import Member

@login_required()
def view_member(request):
    print request.user
    u = User.objects.get(username=request.user)
    m = u.member

    marketplace = get_marketplace(u.member.user_token)
    apps_market = json.loads(marketplace)
    img_source = full_server_address()['url']

    if (CONFIG.DEBUG):
        print "User email: %s" % u.email
        print "Member: %s" % m.member_guid

        print "Member GUID: %s" % (m.member_guid)
        print "User Access Token: %s" % u.member.user_token
#        print "Marketplace Auth: %s" % authenticated
        print "Marketplace info: %s" % apps_market['apps']


    context = {'PAGE_TITLE': 'Member Profile',
                'USER': u,
                'MEMBER': m,
                'GUID': m.member_guid,
                'MARKETPLACE': apps_market['apps'],
                'IMG_SERVER': img_source,
                }
    return render_to_response('member/profile.html', RequestContext(request, context))

@login_required()
def get_ext_id(request):
    print request.user
    u = User.objects.get(username=request.user)
    m = u.member
    guid = m.member_guid

    print "User email: %s" % u.email
    print "Member: %s" % m.member_guid
    print "Pass GUID as %s" % guid

    check_id = validic_check_org(request)
    print "CheckID: %s"  % check_id

    result = ""
    if u.member.ext_uid == "":
        # call validic and allocate user_id
        result = get_validic_user(request, guid)


    context = {'PAGE_TITLE': 'Member Profile',
                'USER': u,
                'MEMBER': m,
                'GUID': m.member_guid,
                'RESULT': result,
    }

    return render_to_response('member/profile.html', RequestContext(request, context))


@login_required()
def get_validic_user(request, guid):
    """
POST https://api.validic.com/v1/organizations/{ORGANIZATION_ID}/users.json
{
  "user": {
    "uid": "{CUSTOMER_USER_ID}"
  },
  "access_token": "{ORGANIZATION_ACCESS_TOKEN}"
}
201
{
  "code": 201,
  "message": "Ok",
  "user": {
    "_id": "{USER_ID}",
    "access_token": "{USER_ACCESS_TOKEN}"
  }
}

    :param u:
    :return:
    """


    content = {
        "user": {
        "uid": guid
        },
        "access_token": CONFIG.V_ACCESS_TOKEN
        }

    json_dumps = json.dumps(content)
    content_encoded = urllib.urlencode(content)
    json_encoded = urllib.quote_plus(json_dumps)

    send_to_prefix = "/v1/organizations/" + CONFIG.V_ORG_ID
    send_to = send_to_prefix + "/users.json"

    address = full_server_address()

    if (CONFIG.DEBUG):
        print "url: %s" % address['url']
        print "GUID: %s" % guid
        print "Org ID: %s" % CONFIG.V_ORG_ID
        print "Server: %s" % CONFIG.V_SERVER
        print "Access Token: %s" % CONFIG.V_ACCESS_TOKEN
        print "Call to: %s" % send_to

    validic = httplib.HTTPSConnection(CONFIG.V_SERVER)
    headers = {"Content-Type": "application/json",
               'Accept': 'application/json',
              }



    r = requests.post( address['url'], data=json.dumps(content), headers=headers)

    data = r.text

    if (CONFIG.DEBUG):
        print "Headers: %s" % headers
        print "Content: %s" % content_encoded
#       print "Status: %s" % r.status
#       print "Reason: %s" % r.reason
        print "Data: %s" % data

#    if r.read('code')==201:
#        print r.reason

    result = data
    return(result)



@login_required()
def validic_check_org(request):
    """
    /v1/organizations/{ORGANIZATION_ID}.json?access_token={ORGANIZATION_ACCESS_TOKEN}
    :param request:
    :return:
    """

    address = full_server_address()
    url = address['url']
    connection = httplib.HTTPSConnection(url)
    headers = {"Content-Type": "application/json",}

    data = urllib.urlencode("")
    site_page = "/v1/organizations/" + CONFIG.V_ORG_ID +".json?access_token=" \
           + CONFIG.V_ACCESS_TOKEN

    connection.request('GET', site_page, data, headers)

    response = connection.getresponse()
    data = response.read()

    if (CONFIG.DEBUG):
        print "Data check org: %s, %s" % (response.status, response.reason)

    return(data)