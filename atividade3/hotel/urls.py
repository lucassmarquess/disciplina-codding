from django.urls import path
from hotel.views.pessoas import listar_pessoas

urlpatterns = [
    path('pessoas/', listar_pessoas, name='listar_pessoas'),
]
