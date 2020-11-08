from django.contrib import admin
from django.urls import path, include
from django.conf import settings


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
    path('', include("Result.urls")),
]
