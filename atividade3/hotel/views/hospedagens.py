from django.shortcuts import render, redirect, get_object_or_404
from hotel.models import Hospedagem, Pessoa, Apartamento

def listar_hospedagens(request):
    hospegadens = Hospedagem.objects.all()

    return render(request, "hotel/hospedagens/listar.html", {'hospegadens': hospegadens})