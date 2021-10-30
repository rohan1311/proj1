
from django.urls import path
from django.urls.conf import re_path

from . import views

urlpatterns = [
    path('', views.UserDataView.as_view(), name = "user_data_new"),
    path('<str:pk>/', views.UserDataDetailView.as_view(), name='user_data_detail'),
]
    # path('data/<str:pk>/', views.user_data_detail, name='user_data_detail'),
    #path('', views.user_data_new, name="user_data_new"),