# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.template import Template , Context, loader
from .models import Car
from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CarModelForm
from .mixin import FormUserNeededMixin

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
    template_name = "basic/car_list.html"
    #template_name = 'templates/basic/car_list.html'
    queryset = Car.objects.all()

def get_queryset(self,*args,**kwargs):
        qs = Car.objects.all()
    #    print self.request.GET()
        query= self.request.GET.get("q",None)
    #    print query
        if query is not None:
            qs=qs.filter(

                        Q(make__icontains=query)|
                        Q(Type__icontains= query)|
                        Q(year__icontains= query)|
                        Q(colour__icontains= query)|
                        Q(price__icontains= query)


                        )
        return qs

def get_context_data(self,*args, **kwargs):
#    context = super(car_list, self).get_context_data(*args,**kwargs)
    context = super(CarListView, self).get_context_data(*args,**kwargs)
#    print context
#    car_list = car_list.objects.all()
    context['create_form'] = CarModelForm()
    context['create_url'] = reverse_lazy("CarCreateView")
    return context

#def upload_file(request):
#    if request.method == 'POST':
#        form = CarModelForm(request.POST, request.FILES)
#        if fomr.is_valid():
            #file is saved
#            form.save()
#            return HttpResponseRedirect('/lists')
#    else:
#        form = CarModelForm()
#        return render(request, 'list.html', context)



class car_detail(DetailView):
     template_name = "basic/car_detail.html"
     queryset = Car.objects.all()

class CarListView(ListView):
    template_name = 'basic/list.html'

class CarCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = CarModelForm
    template_name = "basic/create_view.html"
    success_url = "/list"
    login_url = "/admin"

class CarUpdateView(UpdateView):
    queryset = Car.objects.all()
    form_class = CarModelForm
    template_name = "basic/update_view.html"
    success_url = "/list"

class CArDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = "basic/delete_confirm.html"
#    success_url = reverse_lazy("car_list")
    success_url = reverse_lazy("CarList")

def get_object(self):
        #id = self.kwargs.get("id")
        #print id
        return Car.objects.get(pk=1)
