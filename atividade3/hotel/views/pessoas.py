from django.shortcuts import render, redirect
from hotel.models import Pessoa

# Crie suas views aqui.

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()

    return render(request, "hotel/pessoas/listar.html", {'pessoas': pessoas})

def cadastrar_pessoa(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        contato = request.POST['contato']

        Pessoa.objects.create(
            nome = nome,
            cpf = cpf,
            contato = contato
        )
        return redirect("listar_pessoas")
    return render(request, "hotel/pessoas/cadastrar.html")