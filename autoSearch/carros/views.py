# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.template import Template , Context, loader
from .models import Car
from django.views.generic import DetailView, ListView

# Create your views here.

def prueba(request):
    Context = locals()
    templates = loader.get_template('home.html')
    #return render(request, 'home.html')
    return HttpResponse(templates.render(Context, request))

#def prueba(request):
    #context = locals()
#    return render(request, 'templates/home.html')
#def car_list(request):
#        carros = carros.objects.all()
#        return render(request, 'car_list.html')
#        return render(request, template_name='car_list.html', context={'carros': carros})


class car_list(ListView):
    template_name = "base/estructura.html"
    #template_name = 'templates/basic/car_list.html'
    queryset = Car.objects.all()


class car_detail(DetailView):
     template_name = "basic/car_detail.html"
     queryset = Car.objects.all()


def get_object(self):
        id = self.kwargs.get("id")
        #print id
        return Car.objects.get(id=id)

#def get_context_data(self, **kwargs):
#    context = carro(car_list, self).get_context_data(**kwargs)
#    car_list = car_list.objects.all()
#    context['car_list'] = car_list
#    return context
