from django.conf.urls import url
from .views import user_login, register
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    url(r'^login/$', user_login, name='login'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    url(r'^register/$', register, name='register'),
]
