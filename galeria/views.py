from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Alura Space</h1>') #aqui colocar o site principal o html ou nome do arquivo html pra retonar quando atulizar a pagina
