"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path
from app import views
from django.shortcuts import render,HttpResponse

def custom_404(request, exception):
    """自定义 404 视图函数，渲染 404.html 模板"""
    return render(request, '404.html', status=404)


urlpatterns = [
    # path("admin/", admin.site.urls),
    path("index/", views.index, name="index"),
]
if not settings.DEBUG:
    handler404 = custom_404