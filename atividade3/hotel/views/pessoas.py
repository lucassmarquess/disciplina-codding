from django.shortcuts import render, redirect, get_object_or_404
from hotel.models import Pessoa

# Crie suas views aqui.

def listar_pessoas(request):
    pessoas = Pessoa.objects.filter(ativo=True)

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

def editar_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        contato = request.POST['contato']

        pessoa.nome = nome
        pessoa.cpf = cpf
        pessoa.contato = contato
        pessoa.save()

        return redirect("listar_pessoas")
    return render(request, "hotel/pessoas/editar.html", {"pessoa": pessoa})