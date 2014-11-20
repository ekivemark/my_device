__author__ = 'mark'
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import Template, Context, RequestContext
from django.conf import settings as CONFIG
from django.contrib.auth.decorators import login_required


# Create your views here.
from django.http import HttpResponse, Http404

# Create your views here.
#@login_required(login_url='/#modallogin', redirect_field_name='/home/')
def index(request):

    context = {'modules': CONFIG.TEMPLATE_MODULES,}
    return render_to_response('home/index.html', RequestContext(request, context))
