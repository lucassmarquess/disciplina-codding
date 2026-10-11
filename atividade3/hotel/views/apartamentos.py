from django.shortcuts import render, redirect, get_object_or_404
from hotel.models import Apartamento

def listar_apartamentos(request):
    apartamentos = Apartamento.objects.filter(ativo=True)

    return render(request, "hotel/apartamentos/listar.html", {"apartamentos": apartamentos})