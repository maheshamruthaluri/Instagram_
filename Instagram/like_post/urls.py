from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.like, name='like'),
]
