from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
             #essa parte do views chama a funcao em views com o nome home    
    path('', views.home, name='home'),

    path('usuarios/', views.usuarios, name='listagem_usuarios')
]

#como se fosse a url motada para achar a parte home Rota aqui somento rota
