from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gethelp/', views.get_post, name='posts'),
    path('gethelp/list/', views.get_post, name='postss'),
    path('postedRequests/', views.getAllRequests, name="reqs")
]