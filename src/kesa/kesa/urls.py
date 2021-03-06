"""kesa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from api import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^(?:index.html)?$', views.index, name='index'),
    url(r'^signup/', views.signup, name='signup'),
]

# Authentication
urlpatterns += [
    url(r'^$', views.index, name='index2'),
    url(r'^login/$', 'django.contrib.auth.views.login', { 'template_name': 'api/login.html'}, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^index/$', views.index, name='index'),
    url(r'^(?P<id>\d+)/story/$', views.story, name='story'),
    url(r'^(?P<username>\w+)/profile/$', views.profile, name='profile'),
    url(r'^analytics/$', views.analytics, name='analytics'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^stories/$', views.stories, name='stories'),
    url(r'^create/$', views.create, name='create'),
]
