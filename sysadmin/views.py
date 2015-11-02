from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime


# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('login_welcome.html', {'current_date':now})



def login_index(request):
    now = datetime.datetime.now()
    return render_to_response('index.html', {'current_date':now})