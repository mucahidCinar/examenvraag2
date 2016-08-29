from Examen.models import Examen
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.views import generic


import json

def fbview(request):
    data = A.objects.all().values()
    return render(request, 'test.html', {'data': data})



def save_events_json(request):
    if request.is_ajax():
        if request.method == 'POST':
             'Data: \"%s\"' % request.body
    return HttpResponse("OK")
