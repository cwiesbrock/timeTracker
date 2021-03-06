# -*- coding: utf-8 -*-

"""Timetracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from . import views

urlpatterns = [
	#localhost overview
	url(r'^$', views.index, name = 'index'),
	#employee details
	url(r'^employee/([0-9]+)$/', views.detail, name = 'detail'),
	url(r'^employee/([0-9]*)/$', views.detail, name = 'detail'),
	url(r'^employee/([0-9]*)/(start)/$', views.book, name = 'book'),
	url(r'^employee/([0-9]*)/(end)/$', views.book, name = 'book'),
    url(r'^employee/([0-9]*)/booking/([0-9]*)/(delete)/$', views.booking, name = 'bookingChange')
    ]
