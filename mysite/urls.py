"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    url(r'^', include('main.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login, {'template_name': 'register/login.html'}, name="login"),
    url(r'^signup/', include('register.signupurls')),
    url(r'^meet_participants/', include('voting.urls')),
    url(r'^logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout"),
    url(r'^results/', include('results.urls')),
    url(r'^eliminate/', include('eliminate.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
