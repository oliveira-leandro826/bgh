from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def introducao(request):
    return render(request, 'introducao.html', {})    
