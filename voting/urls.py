from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^participant/$', views.index, name='index'),
    url(r'^participant/(?P<pk>\d+)/$', login_required(views.voteregister), name='vote')]
