from django.urls import path
from . import views

urlpatterns = [
    # path(URL, 関数またはクラス, name=URL名称)
    path('', views.post_list, name='post_list'),
]