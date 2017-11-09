
from django.conf.urls import url, include
from .views import prueba
from carros import views
from autoSearch import urls

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', prueba, name='index'),
    #url(r'^car_list/', views.car_list, name='car_list'),
    #url(r'^carros/', include('carros.urls', namespace='carros', app_name='autos')),

]
