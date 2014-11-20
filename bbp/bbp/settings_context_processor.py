"""
settings_context_processor.py

Use this file to define values from the settings and local_settings files to be used in templates

"""
__author__ = 'mark'

from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured

def config_settings(request):
    config_dict = {
    }

    return config_dict


def settings(request):
    """
    Adds the settings specified in settings.TEMPLATE_VISIBLE_SETTINGS to
    the request context.
    Add the names of any parameters specified in settings.py to
    TEMPLATE_VISIBLE_SETTINGS.
    Variables must be defined before being referenced in TEMPLATE_VISIBLE_SETTINGS
    These values can then be used in templates using {{ VARIABLE }}.
    """
    new_settings = {}
    #print django_settings.TEMPLATE_VISIBLE_SETTINGS
    for attr in getattr(django_settings, "TEMPLATE_VISIBLE_SETTINGS", ()):
        try:
            new_settings[attr] = getattr(django_settings, attr)
        except AttributeError:
            m = "TEMPLATE_VISIBLE_SETTINGS: '{0}' does not exist".format(attr)
            raise ImproperlyConfigured(m);
    return new_settings