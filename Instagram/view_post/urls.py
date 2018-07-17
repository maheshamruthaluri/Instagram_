from django.conf.urls import url
from . import views
#   app_name = 'view_post'
urlpatterns = [
    url(r'^$', views.post, name='post'),
]
