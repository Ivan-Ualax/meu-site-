from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def projetos(request):
    return render(request, 'projetos.html')

def sobre(request):
    return render(request, 'sobre.html')