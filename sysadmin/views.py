from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.utils import timezone
from sysadmin.models import Loginmanagement
from django.core import serializers

import datetime


# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('login_welcome.html', {'current_date':now})



def login_index(request):
    current_date = datetime.datetime.now()
    timezone_name = timezone.get_current_timezone_name()
    return render_to_response('index.html', locals())

def register_index(request):
        current_date = datetime.datetime.now()
        timezone_name = timezone.get_current_timezone_name()
        return render_to_response('register_form.html', locals())

def register_new_user(request):
        login_list = Loginmanagement.objects.all()
        login_data = serializers.serialize("json", login_list)
        # return HttpResponse(login_data, content_type='application/json')
        return render_to_response('register_form.html', locals())
