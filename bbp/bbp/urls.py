from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import ApiEndpoint


urlpatterns = patterns('',
    # Examples:
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),


    url(r'^$', 'bbp.views.home', name='home'),
    url(r'^about/$', 'bbp.views.about', name='about'),
    url(r'^faq/$', 'bbp.views.faq', name='faq'),
    url(r'^contact/$', 'bbp.views.contact', name='contact'),
    url(r'^terms/$', 'bbp.views.terms', name='terms'),
    url(r'^privacy/$', 'bbp.views.privacy', name='privacy'),
    url(r'^accounts/profile/$', 'bbp.views.profile', name='profile'),




    # OAuth2 Provider
    # url(r'^oauth2/', include('provider.oauth2.urls', namespace = 'oauth2')),

    # OAuth Provider
    # http://django-oauth-toolkit.readthedocs.org/en/latest/tutorial/tutorial_01.html
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')), # look ma, I'm a provider!
    url(r'^api/hello', ApiEndpoint.as_view()),  # and also a resource server!


    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
