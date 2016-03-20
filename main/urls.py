"""leThai URL Configuration

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
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views
from contact import views as contact_views
from profiles import views as profile_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.index, name='index'),
    url(r'^contact/', contact_views.about, name='contact'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^profile/', profile_views.profile, name='profile'),
]
