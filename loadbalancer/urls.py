"""loadbalancer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import apis,app
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.sample, name='home'),
    path('router/', apis.host_routing, name='router'),
    path('server1/', apis.server1_path, name='server1-url'),
    path('server2/',apis.server2_path,name='server2-url'),
    path('/healthcheck',app.healthcheck,name="healthcheck")
]
