#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Kun Jia
# date: 8/3/17
# email: me@jarrekk.com

"""project_name URL Configuration

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
import os

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

from .views import *

urlpatterns = []

# debug tool route
if settings.DEBUG:
    import debug_toolbar
    from rest_framework_swagger.views import get_swagger_view

    schema_view = get_swagger_view(title='Pastebin API')

    urlpatterns += [
        url(r'^swagger/', schema_view),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

# Admin application route
# Be used in development and test environment
if os.environ.get('ENV', 'production') != 'production':
    urlpatterns += [
        url(r'^admin/', admin.site.urls),
    ]

# custom url patterns
urlpatterns += [
    url(r'^$', view=IndexView.as_view()),

    # Django all-auth application
    url(r'^accounts/', include('allauth.urls')),

    # Rest API JWT
    url(r'^api/auth/', obtain_jwt_token),

    # REST API applications
    url(r'^api/users/', include('accounts.api_urls'),),

    # Normal applications
    url(r'^users/', include('accounts.urls'),),

]
