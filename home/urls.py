from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('perfil/', views.perfil_user, name='home'),
    path('quiz/', views.quiz_home, name='home'),
]