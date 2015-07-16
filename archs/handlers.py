from django.shortcuts import render_to_response
from django.template import RequestContext
#from piston.handler import BaseHandler
from django.http import HttpResponse
import string
from django.core.exceptions import ValidationError
import subprocess
import sys, httplib2, json, os;

#class getBuildingsHandler(BaseHandler):
    #allowed_methods = ('GET',)
    #model = Building

    #def read(self, request):
        #try:
     #return "hello world"
            #return Building.objects
        #except Building.DoesNotExist:
            #return "No buildings available"
