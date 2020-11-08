from django.urls import path, include#include쓰려면 임포트해주어야함
from . import views # 점은 현재폴더라는 의미, 현재폴더에서  뷰라는 모듈을 가져와라라는 의미, 거기에 있는 인덱스라는 함수가 실행되도록해라
from django.conf import settings


urlpatterns = [
	path('main/', views.index),
	path('', include("Lv1.urls")),
    
		#include-앱에 대해 접속을 처리할 때 반드시 기입해줘야하는것 
  #$는 빈경로 (로컬호스트 8000뒤에 아무것도 안붙이고 접속하는경우 views.index가 실행되도록 만들라는 의미 )
]
