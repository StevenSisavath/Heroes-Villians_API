from django.urls import path
from . import views

urlpatterns = [
    path('', views.super_list),
    path('', views.super_detail)
]