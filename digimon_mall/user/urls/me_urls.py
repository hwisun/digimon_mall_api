from django.urls import path

from ..api import views

urlpatterns = [
    path('', views.MyView.as_view()),
    path('mons/', views.MyMonsView.as_view()),
]