
from django.conf.urls import url, include
from .views import prueba

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', prueba, name='index'),
]
