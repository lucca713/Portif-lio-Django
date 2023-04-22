from django.shortcuts import render
from .models import Usuario
#funcao para carregar e procurar a pagina certa "parte do View" aqui vai fazer a progrmacao doq fazer na pagina
def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #Exibir todos os usuarios cadastrados em uma nova página

    #colocae dentro de um dicionario porque é assim que o django lê os dados
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #retornar os dados para a pagina de listagem de usuarios

    return render(request,'usuarios/usuarios.html', usuarios)
