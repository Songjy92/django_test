from django.urls import path, include
from docform import views

app_name = 'docform'
urlpatterns = [
    path('', views.index, name = 'index'),  # 다른 URLconf들을 참고할 수 있도록 도와주는 함수,
]
