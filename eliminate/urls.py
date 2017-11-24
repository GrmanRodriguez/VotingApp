from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^participant/(?P<pk>\d+)/$', views.voteattempt, name='eliminate')]
