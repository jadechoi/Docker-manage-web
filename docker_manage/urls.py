"""docker_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
import create.views
import list.views
import delete.views
import update.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stack/create', create.views.create),
    path('', create.views.mainpage),
    path('login', create.views.dockerhub_login),
    path('profile', list.views.profile_inspect),
    path('network/create', create.views.netcreate),
    path('volume/create', create.views.volcreate),
    path('network/list', list.views.network_list),
    path('stack/list', list.views.stack_list),
    path('service/list', list.views.service_list),
    path('service/list/<servicename>', list.views.service_ps),
    path('stack/list/<stackname>', list.views.stack_ps),
    path('network/list/<netname>', list.views.network_inspect),
    path('volume/list/<volname>', list.views.volume_inspect),
    path('volume/list', list.views.volume_list),
    path('stack/delete/<stackname>', delete.views.stack_remove),
    path('network/delete/<netname>', delete.views.net_remove),
    path('volume/delete/<volname>', delete.views.vol_remove),
    path('service/update/<servicename>', update.views.update),
    path('service/rollback/<servicename>', update.views.rollback),
    path('service/scale/<servicename>', update.views.scale),
]
