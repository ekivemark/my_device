My Device 
======

This is a prototype application to create a framework for 
integration with the Validic Device integration platform

The application skeleton is based on:
https://github.com/ekivemark/bbp_oa

This application is written using:

 - Python (2.7)
 - Django (1.7)

It will make use of publicly available libraries.

The packages required are listed in: 

./bbp/config/requirements.txt

This prototype has implemented the OAuth2 tutorial from:
http://django-oauth-toolkit.readthedocs.org/en/latest/tutorial/tutorial_02.html

This provides an OAuth2 protected API Endpoint.


# Important

django/http/response.py causes an error in OAuth2 authentication.

The issue is that in Django 1.7 the http/response.py changed from
using mimetype to content_type.

OAuth2 will work if you patch any reference to *mimetype* to *content_type*.

# oauth2 testing

Using curl to test the OAuth2 provider can hit issues resulting in 
{"error": "invalid_client"} or a bash error. The cause is the 
appearance of special characters ($ : = ). You can escape them with a
\ prefix. The other alternative is to replace the Client ID and 
Client Secret with character strings that avoid special characters.

