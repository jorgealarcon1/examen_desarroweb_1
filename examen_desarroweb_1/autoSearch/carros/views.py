# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.template import Template , Context, loader

# Create your views here.

def prueba(request):
    Context = locals()
    templates = loader.get_template('home.html')
    return HttpResponse(templates.render(Context, request))

#def prueba(request):
    #context = locals()
#    return render(request, 'templates/home.html')
