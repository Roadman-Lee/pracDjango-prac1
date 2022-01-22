# startapp 시 urls.py는 만들어지지 않기 때문에 개발자가 만든다.
from django.urls import path
from pracapp import views # 동일 app폴도의 views.py의 함수를 사용하기위한 views import!!

urlpatterns = [
    # 상위 폴더(practice)의 path를 통하여(include 모듈에 의한) 해당 urls를 사용할 수 있게된다. 
    path('', views.index), # 해당 app폴더의 views.py에 있는 함수를 찾는다. views.함수이름 으로 사용한다.
    path('create/', views.create),
    path('read/<id>/', views.read),
] 