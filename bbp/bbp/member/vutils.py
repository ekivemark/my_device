__author__ = 'mark'
"""
Validic Integration utilities

Library for Validic Device Integration. Based on:
https://validic.com/api/docs

"""
from django.conf import settings as CONFIG
from django.http.response import HttpResponse
import requests
import httplib
import json

def get_organization(self):
    """

    :return: result{}
    """

    # Server name and optional port without http:// or https:// prefix
    server = CONFIG.V_Server
    if CONFIG.V_Secure == True:
        prefix = "https://"
    else:
        prefix = "http://"

    url = prefix + CONFIG.V_Server

    code = 200
    reason = "ok"


    result = {
        'code' : code,
        'reason': reason,
        'url' : url,

    }


    return(result)

def full_server_address():
    """
    Build the full server address using settings from settings.py
    :return: dict with code, reason and url
    """

    if (CONFIG.V_SECURE):
        prefix = "https://"
    else:
        prefix = "http://"

    try:
        v_port = CONFIG.V_PORT
    except AttributeError:
        v_port = 0

    if v_port > 0:
        suffix = ":" + str(CONFIG.V_PORT)
    else:
        suffix = ""


    url = prefix + CONFIG.V_SERVER + suffix


    if CONFIG.V_SERVER == "":
        code = 400
        reason = "V_SERVER not defined in settings.py"
    else:
        code = 200
        reason = "ok"


    result = {
        'status' : code,
        'reason': reason,
        'url' : url,
        }

    if (CONFIG.DEBUG):
        print "v_port: %s" % v_port
        print "Secure Mode: %s" % CONFIG.V_SECURE
        print "Server: %s" % CONFIG.V_SERVER
        print "v_port: %s" % v_port
        print "Suffix: %s" % suffix
        print "Result: %s" % result


    return (result)


def marketplace_auth(user_access_token):
    """
    GET https://app.validic.com/{ORGANIZATION_ID}/{USER_ACCESS_TOKEN}

    """
    server_address = full_server_address()['url']
    page = "/" + CONFIG.V_ORG_ID + "/" + user_access_token

    validic = httplib.HTTPSConnection(CONFIG.V_SERVER)
    headers = {"Content-Type": "application/json",
               'Accept': 'application/json',
              }

    content = {}

    url = server_address + page
    r = requests.get( url, data=json.dumps(content), headers=headers)

    result = r.text

    if (CONFIG.DEBUG):
        print "Data: %s" % result

    return(result)

def get_marketplace(user_access_token):
    """
GET https://api.validic.com/v1/organizations/
{ORGANIZATION_ID}
/apps.json?authentication_token=
{USER_ACCESS_TOKEN}
&access_token={ORGANIZATION_ACCESS_TOKEN}

https://api.validic.com/v1/organizations/
53b2d744d4391c28f0000004
/apps.json?authentication_token=
JK3Gq56GoEdtsnSXHyCC
&access_token=
e1c95b3a390b442f06efd266d782734ad886f7f7117453ebabf540b5e73d78d7


    :param user_access_token:
    :return: summary dict
    """

    server_address = full_server_address()['url']
    page = "/v1/organizations/" + CONFIG.V_ORG_ID + \
           "/apps.json?authentication_token=" + user_access_token + \
           "&access_token=" + CONFIG.V_ACCESS_TOKEN

    validic = httplib.HTTPSConnection(CONFIG.V_SERVER)
    headers = {"Content-Type": "application/json",
               'Accept': 'application/json',
              }

    content = {}

    url = server_address + page

    r = requests.get( url, data=json.dumps(content), headers=headers)

    result = r.text

#    if (CONFIG.DEBUG):
#        print "Data: %s" % result

    return(result)

