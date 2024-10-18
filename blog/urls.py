from django.urls import path
from . import views  # Importa suas views

urlpatterns = [
    path('', views.index, name='index'),  # Para a página inicial
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Para detalhes de um post
    path('about/', views.about, name='about'),  # Para a página de about (opcional)
]
