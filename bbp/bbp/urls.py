from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from django.contrib import admin

from .views import ApiEndpoint
admin.autodiscover()

from rest_framework import viewsets, routers
from rest_framework import permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

# from: http://django-oauth-toolkit.readthedocs.org/en/latest/rest-framework/getting_started.html
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    model = User


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    model = Group


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = patterns('',
    # Login/logout
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),

    # default pages
    url(r'^$', 'bbp.views.home', name='home'),
    url(r'^about/$', 'bbp.views.about', name='about'),
    url(r'^faq/$', 'bbp.views.faq', name='faq'),
    url(r'^contact/$', 'bbp.views.contact', name='contact'),
    url(r'^terms/$', 'bbp.views.terms', name='terms'),
    url(r'^privacy/$', 'bbp.views.privacy', name='privacy'),

    # Link in subsidiary modules
    url(r'^device/', include('device.urls', namespace='device')),
    url(r'^member/', include('bbp.member.urls', namespace='member')),

    # API test -(login_required)
    url(r'^secret$', 'bbp.views.secret_page', name='secret'),
    # http://django-oauth-toolkit.readthedocs.org/en/latest/tutorial/tutorial_03.html

    # OAuth2 Provider
    # url(r'^oauth2/', include('provider.oauth2.urls', namespace = 'oauth2')),

    # OAuth Provider
    # http://django-oauth-toolkit.readthedocs.org/en/latest/tutorial/tutorial_01.html
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')), # look ma, I'm a provider!
    url(r'^api/hello', ApiEndpoint.as_view()),  # and also a resource server!

    # API
    url(r'^1.0/api/', include(router.urls)),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
