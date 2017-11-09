"""autoSearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from carros import views, urls, urls, models
from carros.views import car_list, car_detail



#from .views import templates
    #from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^carros/', include('carros.urls')),
    url(r'^',include('carros.urls', namespace = "templates")),
    url(r'^detail/(?P<pk>[0-9]+)/$', car_detail.as_view(),name='CarDetail'),
    url(r'^list$',car_list.as_view(), name='CarList'),
    #url(r'list/^$', car_list, name='car_list.html'),
    #url(r'^carros/', include('carros.urls', namespace='carros', app_name='autos')),
]
