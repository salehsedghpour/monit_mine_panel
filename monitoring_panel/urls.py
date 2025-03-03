"""monitoring_panel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from login.views import login,logout_view
from dashboard.views import dashboard
from django.conf.urls import url
from monitoring.views import monitoring
from configurations.views import configurations

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', login),
    path('dashboard/',dashboard),
    url(r'^logout/$', logout_view),
    path('monitoring/',monitoring),
    path('configurations/',configurations)
]
