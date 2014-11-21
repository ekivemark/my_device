__author__ = 'mark'
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import Template, Context, RequestContext
from django.conf import settings as CONFIG
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse, Http404

# Create your views here.
#@login_required(login_url='/#modallogin', redirect_field_name='/home/')
def home(request):

    context = {'modules': CONFIG.TEMPLATE_MODULES,}
    return render_to_response('home/index.html', RequestContext(request, context))

def about(request):

    context = {'modules': CONFIG.TEMPLATE_MODULES,
               'PAGE_TITLE': 'About',}
    return render_to_response('home/about.html', RequestContext(request, context))

def faq(request):

    context = {'modules': CONFIG.TEMPLATE_MODULES,
               'PAGE_TITLE': 'Frequently Asked Questions',}
    return render_to_response('home/faq.html', RequestContext(request, context))

def contact(request):

    context = {'modules': CONFIG.TEMPLATE_MODULES,
               'PAGE_TITLE': 'Contact Us',}
    return render_to_response('home/contact.html', RequestContext(request, context))

def terms(request):

    context = {'modules': CONFIG.TEMPLATE_MODULES,
               'PAGE_TITLE': 'Terms of Use',}
    return render_to_response('home/terms.html', RequestContext(request, context))

def privacy(request):

    context = {'modules': CONFIG.TEMPLATE_MODULES,
               'PAGE_TITLE': 'Your Privacy Comes First',}
    return render_to_response('home/privacy.html', RequestContext(request, context))

@login_required()
def profile(request):
    u = User(username=request.user)
    print "User: %s" % u.username

    context = {'PAGE_TITLE': 'User Profile', }
    return render_to_response('home/profile.html', RequestContext(request, context))