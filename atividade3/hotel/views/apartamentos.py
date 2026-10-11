from django.shortcuts import render, redirect, get_object_or_404
from hotel.models import Apartamento

def listar_apartamentos(request):
    apartamentos = Apartamento.objects.filter(ativo=True)

    return render(request, "hotel/apartamentos/listar.html", {"apartamentos": apartamentos})

def cadastrar_apartamento(request):
    if request.method == "POST":
        numeracao = request.POST['numeracao']
        preco_diaria = request.POST["preco_diaria"].replace(",", ".")
        tipo = request.POST['tipo']

        Apartamento.objects.create(
            numeracao = numeracao,
            preco_diaria = preco_diaria,
            tipo = tipo
        )
        return redirect("listar_apartamentos")
    return render(request, "hotel/apartamentos/cadastrar.html")

def editar_apartamento(request, id):
    apartamento = get_object_or_404(Apartamento, id=id)

    if request.method == "POST":
        numeracao = request.POST['numeracao']
        preco_diaria = request.POST["preco_diaria"].replace(",", ".")
        tipo = request.POST['tipo']

        apartamento.numeracao = numeracao
        apartamento.preco_diaria = preco_diaria
        apartamento.tipo = tipo
        apartamento.save()
        return redirect("listar_apartamentos")
    return render(request, "hotel/apartamentos/editar.html", {'apartamento': apartamento})
