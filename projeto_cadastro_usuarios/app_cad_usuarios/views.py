from django.shortcuts import render

#funcao para carregar e procurar a pagina certa "parte do View" aqui vai fazer a progrmacao doq fazer na pagina
def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    pass