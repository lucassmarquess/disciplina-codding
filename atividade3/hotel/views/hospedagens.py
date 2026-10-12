from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Max
from django.db.models import Q
from django.utils import timezone
from django.db import transaction
from hotel.models import Hospedagem, Pessoa, Apartamento

def listar_hospedagens(request):
    hospedagens = Hospedagem.objects.all()

    return render(request, "hotel/hospedagens/listar.html", {'hospedagens': hospedagens})

def cadastrar_hospedagem(request):
    pessoas = Pessoa.objects.filter(ativo=True)
    apartamentos = Apartamento.objects.filter(ativo=True, status=False)
    erro = None

    if request.method == 'POST':
        apartamento_id = request.POST.get('apartamento')
        pessoas_ids = request.POST.getlist('pessoas')

        # Evita selecionar a mesma pessoa mais de uma vez
        pessoas_ids = list(dict.fromkeys(pessoas_ids))

        if not apartamento_id or not pessoas_ids:
            erro = 'Selecione um apartamento e pelo menos uma pessoa.'
        else:
            apartamento = Apartamento.objects.filter(
                id=apartamento_id,
                ativo=True
            ).first()

            pessoas_selecionadas = list(
                pessoas.filter(id__in=pessoas_ids)
            )

            if not apartamento:
                erro = 'Apartamento inválido.'
            elif len(pessoas_selecionadas) != len(pessoas_ids):
                erro = 'Uma ou mais pessoas selecionadas são inválidas.'
            else:
                tipo = apartamento.tipo.strip().lower()

                limites = {
                    'padrão': 2,
                    'padrao': 2,
                    'luxo': 3,
                    'master': 4
                }

                limite = limites.get(tipo, 0)

                if limite == 0:
                    erro = 'O tipo do apartamento não possui um limite configurado.'
                elif len(pessoas_selecionadas) > limite:
                    erro = f'Esse apartamento permite no máximo {limite} pessoas.'
                else:
                    with transaction.atomic():
                        maior = Hospedagem.objects.aggregate(
                            maior=Max('numeracao')
                        )['maior']

                        numeracao = (maior or 0) + 1

                        for pessoa in pessoas_selecionadas:
                            Hospedagem.objects.create(
                                numeracao=numeracao,
                                pessoa=pessoa,
                                apartamento=apartamento
                            )
                        apartamento.status=True
                        apartamento.save()

                    return redirect('listar_hospedagens')

    return render(
        request,
        'hotel/hospedagens/cadastrar.html',
        {
            'pessoas': pessoas,
            'apartamentos': apartamentos,
            'erro': erro
        }
    )

def editar_hospedagem(request, id):
    hospedagem = get_object_or_404(Hospedagem, id=id)

    pessoas = Pessoa.objects.filter(ativo=True)

    # Exibe apartamentos disponíveis e o apartamento atual.
    apartamentos = Apartamento.objects.filter(ativo=True).filter(
        Q(status=False) | Q(id=hospedagem.apartamento_id)
    )

    erro = None

    if request.method == 'POST':
        pessoa_id = request.POST.get('pessoa')
        apartamento_id = request.POST.get('apartamento')

        pessoa = pessoas.filter(id=pessoa_id).first()
        apartamento_novo = apartamentos.filter(id=apartamento_id).first()

        if not pessoa or not apartamento_novo:
            erro = 'Selecione uma pessoa e um apartamento válidos.'
        else:
            apartamento_antigo = hospedagem.apartamento

            with transaction.atomic():
                hospedagem.pessoa = pessoa

                if apartamento_novo.id != apartamento_antigo.id:
                    # A mudança de apartamento cria um novo grupo.
                    maior = Hospedagem.objects.aggregate(
                        maior=Max('numeracao')
                    )['maior']

                    hospedagem.numeracao = (maior or 0) + 1
                    hospedagem.apartamento = apartamento_novo
                    apartamento_novo.status = True
                    apartamento_novo.save()

                    # Só libera o antigo se ninguém mais estiver hospedado nele.
                    ainda_ocupado = Hospedagem.objects.filter(
                        apartamento=apartamento_antigo,
                        ativo=True
                    ).exclude(id=hospedagem.id).exists()

                    if not ainda_ocupado:
                        apartamento_antigo.status = False
                        apartamento_antigo.save()

                hospedagem.save()

            return redirect('listar_hospedagens')

    return render(
        request,
        'hotel/hospedagens/editar.html',
        {
            'hospedagem': hospedagem,
            'pessoas': pessoas,
            'apartamentos': apartamentos,
            'erro': erro
        }
    )

def encerrar_hospedagem(request, id):
    hospedagem = get_object_or_404(Hospedagem, id=id)

    if not hospedagem.ativo:
        return redirect('listar_hospedagens')

    data_encerramento = timezone.localdate()
    diarias = max((data_encerramento - hospedagem.data_inicio).days, 1)
    total = hospedagem.apartamento.preco_diaria * diarias

    if request.method == 'POST':
        with transaction.atomic():
            hospedagem.data_final = timezone.localdate()
            hospedagem.ativo = False
            hospedagem.save(update_fields=['data_final', 'ativo'])

            apartamento = hospedagem.apartamento

            ainda_ocupado = Hospedagem.objects.filter(
                apartamento=apartamento,
                ativo=True
            ).exists()

            if not ainda_ocupado:
                apartamento.status = False
                apartamento.save(update_fields=['status'])

        return redirect('listar_hospedagens')

    return render(
        request,
        'hotel/hospedagens/encerrar.html',
        {
            'hospedagem': hospedagem,
            'diarias': diarias,
            'total': total,
            'data_encerramento': data_encerramento
        }
    )