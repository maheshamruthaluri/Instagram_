from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^logout/$', views.logout, name='logout'),
]