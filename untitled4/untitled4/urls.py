"""untitled4 URL Configuration

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
from django.conf.urls import url
# from django.contrib import admin
from backend import views
# from django.urls import path

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^v1/camera_address', views.get_test_address),
    url(r'^v1/add_raspberry', views.register_rasp),
    url(r'^v1/get_cameras/(?P<owner>[-\w]+)/$', views.get_raspis),
    url(r'^v1/connect', views.connect_rasp_with_user),
]
