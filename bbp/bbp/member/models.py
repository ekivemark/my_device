__author__ = 'mark'
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Member(models.Model):
    member = models.ForeignKey(User, unique=True)
    member_guid = models.CharField(max_length=200, blank=True, null=True)
    user_token = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):              # __un
    # icode__ on Python 2

        return self.member_guid

User.member = property(lambda u:Member.objects.get_or_create(member=u)[0])



