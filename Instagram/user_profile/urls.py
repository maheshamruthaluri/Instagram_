from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^(?P<pk>\d+)/$', views.profile, name='profile'),
]

