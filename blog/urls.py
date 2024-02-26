from django.urls import path
from . import views

urlpatterns = [
    # path(URL, 関数またはクラス, name=URL名称)
    path('', views.post_list, name='post_list'),
    
    # post/ はURLが post に続けて / で始まることを意味します。
    # <int:pk> – この部分はDjangoは整数の値を期待し、その値がpkという名前の変数でビューに渡されることを意味しています。
    # / – それからURLの最後に再び / が必要です。  
    # つまり'http://127.0.0.1:8000/post/5/'を入力すると、Djangoはpost_detailというビューを探していると理解します。  
    # そしてpkが5という情報をそのビューに転送します。
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
    path('post/new/', views.post_new, name='post_new'),
    
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]