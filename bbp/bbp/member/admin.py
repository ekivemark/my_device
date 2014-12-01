__author__ = 'mark'
"""
Admin functions for extended user model
https://docs.djangoproject.com/en/1.7/topics/auth/customizing/#a-full-example
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from models import Member

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class MemberInline(admin.StackedInline):
    model = Member
    can_delete = False
    verbose_name_plural = 'member'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (MemberInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)