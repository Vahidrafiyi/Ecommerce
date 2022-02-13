"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from online_course.views import my_view
from django.conf import settings
from django.conf.urls.static import static
from consulting.views import ConslutFormAPI
urlpatterns = [
    path('admin/', admin.site.urls),
    path('online_course/', include('online_course.urls')),
    path('', my_view),
    path('ticket/', include('tick.urls')),
    path('blog/', include('blog.urls')),
    path('event_log/', include('event_log.urls')),
    path('consult', ConslutFormAPI.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
