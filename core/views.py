from django.shortcuts import render
from .models import Especie, Imagem, Acesso

def index(request):
    return render(request, 'index.html', {})

def introducao(request):
    return render(request, 'introducao.html', {})  

def colecoes(request):
    especies = Especie.objects.all()
    imagens = Imagem.objects.all()

    contexto = {'especies': especies, 'imagens': imagens}

    return render(request, 'colecoes.html', contexto)      
