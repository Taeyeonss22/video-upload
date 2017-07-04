from django.conf.urls import url
from .views import subir_video, index
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^upload/$', subir_video, name='subir_video'),
]
