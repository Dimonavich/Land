"""Land URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path
from django.conf.urls import include

from datetime import datetime
import django.contrib.auth.views

import home.forms
from home.views import register




urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'^$', include('home.urls')),
    re_path(r'Video/', include('video.urls')),
    re_path(r'history/', include('history.urls')),
    re_path(r'galery/', include('galery.urls')),
    re_path(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'home/login.html',
            'authentication_form': home.forms.BootstrapAuthenticationForm,
            'extra_context':
                {
                    'title': 'Log in',
                    'year': datetime.now().year,
                }
        },
        name='login'),
    re_path(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    re_path(r'register/', register),
]
