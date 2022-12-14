from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('jogador/<int:pk>/', views.jogador, name='jogador'),
    path('jogadorEdit/<int:pk>/', views.edit, name='edit'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('formConexao/', views.formConexao, name='formConexao'),
    path('createConexao/', views.createConexao, name='createConexao'),
    path('conexao/<int:pk>/', views.conexao, name='conexao'),
    path('conexoes/<int:pk>/', views.conexoes, name='conexoes'),
]