bbp_oa (BlueButton Plus with OAuth 2.0)
======

This is a prototype application to create a framework for 
distributing BlueButtonPlus data via an OAuth2.0 controlled API.

This application is written using:
- Python (2.7)
- Django (1.7)

It will make use of publicly available libraries.

The packages required are listed in: 

./bbp/config/requirements.txt


Important:

django/http/response.py causes an error in OAuth2 authentication.

The issue is that in Django 1.7 the http/response.py changed from
using mimetype to content_type.

OAuth2 will work if you patch any reference to mimetype to content_type.


