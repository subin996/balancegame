"""webgame URL Configuration

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
from django.urls import path , include


urlpatterns = [
    path('', include("main.urls")),#include-앱에 대해 접속을 처리할 때 반드시 기입해줘야하는것 
    path('admin/', admin.site.urls),#어드민이라는 주소를 접속할 때 어드민이라는 녀석이 처리해라
    path('', include("Lv1.urls")),
    path('', include("Lv2.urls")),
    path('', include("Lv3.urls")),
    path('', include("Lv4.urls")),
    path('', include("Lv5.urls")),
    path('', include("Lv6.urls")),
    path('', include("Lv7.urls")),
    path('', include("Lv8.urls")),
    path('', include("Result.urls")),#어드민이라는 주소를 접속할 때 어드민이라는 녀석이 처리해라
]
