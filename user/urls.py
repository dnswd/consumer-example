from django.urls import path

from user import views

urlpatterns = [
    path('<str:name>/', views.index, name='index'),
]