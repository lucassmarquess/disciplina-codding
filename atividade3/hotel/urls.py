from django.urls import path
from hotel.views.pessoas import listar_pessoas, cadastrar_pessoa, editar_pessoa, excluir_pessoa

urlpatterns = [
    path('pessoas/', listar_pessoas, name='listar_pessoas'),
    path('pessoas/cadastrar', cadastrar_pessoa, name='cadastrar_pessoa'),
    path('passoas/<int:id>/editar', editar_pessoa, name='editar_pessoa'),
    path('pessoas/<int:id>/excluir', excluir_pessoa, name='excluir_pessoa'),
]
