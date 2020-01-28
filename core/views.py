from django.shortcuts import render
from .models import Especie, Imagem, Acesso

def index(request):
    return render(request, 'index.html', {})

def introducao(request):
    return render(request, 'introducao.html', {})  

def colecoes(request):
    especies = Especie.objects.all()

    contexto = {'especies': especies}

    return render(request, 'colecoes.html', contexto)   

def especie(request, id):
    especie = Especie.objects.get(pk=id)
    acessos = Acesso.objects.filter(especie=especie.pk)

    contexto = {'especie': especie, 'acessos': acessos}

    return render(request, 'especie.html', contexto)
