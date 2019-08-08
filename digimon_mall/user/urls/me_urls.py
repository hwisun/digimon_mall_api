from django.urls import path

from ..api import views

urlpatterns = [
    path('', views.MymeView.as_view()),
    path('mons/', views.MyitemsView.as_view()),
]