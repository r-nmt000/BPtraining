#!/usr/bin/env python

from django.http import HttpResponse
from necommend.models import Neco 

def neco_list(request):
  _list = Neco.serialize_list('json')
  return HttpResponse(_list, mimetype='application/json')

def neco_detail(request, neco_id):
  _object = Neco.serialize_object('json', neco_id)
  return HttpResponse(_object, mimetype='application/json')
