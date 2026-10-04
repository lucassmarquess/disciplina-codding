from django.shortcuts import render
from hotel.models import Pessoa

# Crie suas views aqui.

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()

    return render(request, "hotel/pessoas/listar.html", {'pessoas': pessoas})
