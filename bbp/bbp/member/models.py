__author__ = 'mark'
"""
User Profile Extension based on One-to-One fields code in Django Docs here:
https://docs.djangoproject.com/en/1.7/topics/auth/customizing/
"""
from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

class Member(models.Model):
    user = models.OneToOneField(User)
    member_guid = models.CharField(max_length=100, null=True, blank=True)
    ext_uid = models.CharField(max_length=100, null=True, blank=True)
    user_token = models.CharField(max_length=100, null=True, blank=True)

