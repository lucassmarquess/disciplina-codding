from django.urls import path
from hotel.views.pessoas import listar_pessoas, cadastrar_pessoa, editar_pessoa, excluir_pessoa
from hotel.views.apartamentos import listar_apartamentos, cadastrar_apartamento, editar_apartamento, excluir_apartamento
from hotel.views.hospedagens import listar_hospedagens, cadastrar_hospedagem, editar_hospedagem, encerrar_hospedagem

urlpatterns = [
    #pessoas
        path('pessoas/', listar_pessoas, name='listar_pessoas'),
        path('pessoas/cadastrar', cadastrar_pessoa, name='cadastrar_pessoa'),
        path('passoas/<int:id>/editar', editar_pessoa, name='editar_pessoa'),
        path('pessoas/<int:id>/excluir', excluir_pessoa, name='excluir_pessoa'),
    #apartamentos
        path('apartamentos/', listar_apartamentos, name='listar_apartamentos'),
        path('apartamentos/cadastrar', cadastrar_apartamento, name='cadastrar_apartamento'),
        path('apartamentos/<int:id>/editar', editar_apartamento, name='editar_apartamento'),
        path('apartamentos/<int:id>/excluir', excluir_apartamento, name='excluir_apartamento'),
    #hospedagens
        path('hospedagens/', listar_hospedagens, name= 'listar_hospedagens'),
        path('hospedagens/cadastrar', cadastrar_hospedagem, name='cadastrar_hospedagem'),
        path('hospedagens/<int:id>/editar', editar_hospedagem, name='editar_hospedagem'),
        path('hospedagens/encerrar/<int:id>/', encerrar_hospedagem, name='encerrar_hospedagem'),
    ]
