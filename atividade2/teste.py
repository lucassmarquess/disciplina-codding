from main import Carro,Moto, Caminhao, Fisica, Juridica, Contrato, Condutor, Manutencao
from datetime import datetime

veiculos = {}
clientes = {}
contratos = {}
condutores = {}
manutencoes = {}

def gerar_id(dicionario):
    if not dicionario:
        return 1
    return max(dicionario.keys()) + 1

def veiculo_disponivel(veiculo_id):
    for contrato in contratos.values():
        if contrato.veiculo_id == veiculo_id and contrato.status == "ativo":
            return False
    return True

while True:
    print("\n===== SISTEMA DE LOCAÇÃO =====")
    print("1 - Cadastrar carro")
    print("2 - Cadastrar moto")
    print("3 - Cadastrar caminhão")
    print("4 - Listar veículos")
    print("5 - Cadastrar pessoa física")
    print("6 - Cadastrar pessoa jurídica")
    print("7 - Listar clientes")
    print("8 - Cadastrar condutor")
    print("9 - Listar condutores")
    print("10 - Criar contrato")
    print("11 - Listar contratos")
    print("12 - Finalizar contrato")
    print("13 - Cancelar contrato")
    print("14 - Excluir contrato")
    print("15 - Cadastrar manutenção")
    print("16 - Listar manutenções")
    print("0 - Sair")
    print("\n==============================")


    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            print("\n===== CADASTRO DE CARRO =====")
            id = gerar_id(veiculos)
            placa = input("Placa: ")
            modelo = input("Modelo: ")
            ano = int(input("Ano: "))
            valor_diaria = float(input("Valor da diária: "))
            quantidade_portas = int(input("Quantidade de portas: "))
            cambio = input("Câmbio: ")

            carro = Carro(id, quantidade_portas, cambio, placa, modelo, ano, valor_diaria)
            veiculos[id] = carro
            print(f"Carro cadastrado com sucesso! ID: {id}")

        case "2":
            print("\n====== CADASTRO DE MOTO ======")

            id = gerar_id(veiculos)
            placa = input("Placa: ")
            modelo = input("Modelo: ")
            ano = int(input("Ano: "))
            valor_diaria = float(input("Valor da diária: "))
            cilindradas = int(input("Cilindradas: "))
            partida = input("Tipo de partida: ")

            moto = Moto(id, cilindradas, partida, placa, modelo, ano, valor_diaria)
            veiculos[id] = moto
            print(f"Moto cadastrada com sucesso! ID: {id}")

        case "3":
            print("\n==== CADASTRO DE CAMINHÃO ====")

            id = gerar_id(veiculos)
            placa = input("Placa: ")
            modelo = input("Modelo: ")
            ano = int(input("Ano: "))
            valor_diaria = float(input("Valor da diária: "))
            quantidade_carga = float(input("Quantidade de carga: "))
            quantidade_eixos = int(input("Quantidade de eixos: "))

            caminhao = Caminhao(id, quantidade_carga, quantidade_eixos, placa, modelo, ano, valor_diaria)
            veiculos[id] = caminhao
            print(f"Caminhão cadastrado com sucesso! ID: {id}")

        case "4":
            if not veiculos:
                print("Cadastre um veículo primeiro.")
            else:
                print("\n===== LISTA DE VEÍCULOS =====")
                for veiculo in veiculos.values():
                    print(f"\nID: {veiculo.id}")
                    print(f"Tipo: {type(veiculo).__name__}")
                    print(f"Placa: {veiculo.placa}")
                    print(f"Modelo: {veiculo.modelo}")
                    print(f"Ano: {veiculo.ano}")
                    print(f"Valor da diária: R$ {veiculo.valor_diaria:.2f}")

        case "5":
            print("\n=== CADASTRO PESSOA FÍSICA ===")
            id = gerar_id(clientes)
            nome = input("Nome: ")
            documento = input("CPF: ")
            telefone = input("Telefone: ")

            cliente = Fisica(id, nome, None, documento, telefone)
            clientes[id] = cliente
            print(f"Pessoa física cadastrada com sucesso! ID: {id}")

        case "6":
            print("\n== CADASTRO PESSOA JURÍDICA ==")
            id = gerar_id(clientes)
            razao_social = input("Razão social: ")
            documento = input("CNPJ: ")
            telefone = input("Telefone: ")

            cliente = Juridica(id, None, razao_social, documento, telefone)
            clientes[id] = cliente
            print(f"Pessoa jurídica cadastrada com sucesso! ID: {id}")

        case "7":
            if not clientes:
                print("Cadastre um cliente primeiro.")
            else:
                print("\n===== LISTA DE CLIENTES =====")
                for cliente in clientes.values():
                    print(f"\nID: {cliente.id}")
                    print(f"Tipo: {type(cliente).__name__}")
                    print(f"Documento: {cliente.documento}")
                    print(f"Telefone: {cliente.telefone}")
                    if isinstance(cliente, Fisica):
                        print(f"Nome: {cliente.nome}")
                    else:
                        print(f"Razão social: {cliente.razao_social}")

        case "8":
            print("\n==== CADASTRO DE CONDUTOR ====")

            id = gerar_id(condutores)
            nome = input("Nome do condutor: ")
            cnh = input("CNH: ")

            condutor = Condutor(id, nome, cnh)
            condutores[id] = condutor
            print(f"Condutor cadastrado com sucesso! ID: {id}")

        case "9":
            if not condutores:
                print("Cadastre um condutor primeiro.")
            else:
                print("\n==== LISTA DE CONDUTORES ====")
                for condutor in condutores.values():
                    print(f"\nID: {condutor.id}")
                    print(f"Nome: {condutor.nome}")
                    print(f"CNH: {condutor.cnh}")
                    print(f"Contrato: {condutor.contrato_id}")

        case "10":
            if not clientes:
                print("Cadastre um cliente primeiro.")
            elif not veiculos:
                print("Cadastre um veículo primeiro.")
            elif not condutores:
                print("Cadastre um condutor primeiro.")
            else:
                print("\n==== CADASTRO DE CONTRATO ====")
                id = gerar_id(contratos)
                cliente_id = int(input("ID do cliente: "))
                cliente = clientes.get(cliente_id)

                if not cliente:
                    print("Cliente não encontrado.")
                else:
                    veiculo_id = int(input("ID do veículo: "))
                    veiculo = veiculos.get(veiculo_id)

                    if not veiculo:
                        print("Veículo não encontrado.")
                    elif not veiculo_disponivel(veiculo_id):
                        print("Esse veículo já possui um contrato ativo.")
                    else:
                        condutor_id = int(input("ID do condutor: "))
                        condutor = condutores.get(condutor_id)

                        if not condutor:
                            print("Condutor não encontrado.")
                        elif condutor.contrato_id is not None:
                            print("Esse condutor já está vinculado a um contrato.")
                        else:
                            data_inicio = input("Data de início (DD/MM/AAAA): ")
                            data_termino = input("Data de término (DD/MM/AAAA): ")

                            try:
                                inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
                                termino = datetime.strptime(data_termino, "%d/%m/%Y")

                                if termino <= inicio:
                                    print("A data de término deve ser posterior à data de início.")
                                else:
                                    contrato = Contrato(id, data_inicio, data_termino, 0, "ativo", cliente_id, veiculo_id, condutor_id)
                                    contrato.calcular_valor_total(veiculo.valor_diaria)
                                    contratos[id] = contrato
                                    condutor.contrato_id = id
                                    print(f"Contrato criado com sucesso! ID: {id}")
                                    print(f"Valor total: R$ {contrato.valor_total:.2f}")
                            except ValueError:
                                print("Data inválida. Use o formato DD/MM/AAAA.")

        case "11":
            if not contratos:
                print("Cadastre um contrato primeiro.")
            else:
                print("\n===== LISTA DE CONTRATOS =====")
                for contrato in contratos.values():
                    print(f"\nID: {contrato.id}")
                    print(f"Cliente ID: {contrato.cliente_id}")
                    print(f"Veículo ID: {contrato.veiculo_id}")
                    print(f"Condutor ID: {contrato.condutor_id}")
                    print(f"Data de início: {contrato.data_inicio}")
                    print(f"Data de término: {contrato.data_termino}")
                    print(f"Valor total: R$ {contrato.valor_total:.2f}")
                    print(f"Status: {contrato.status}")

        case "12":
            if not contratos:
                print("Cadastre um contrato primeiro.")
            else:
                print("\n===== FINALIZAR CONTRATO =====")
                id = int(input("ID do contrato: "))
                contrato = contratos.get(id)

                if not contrato:
                    print("Contrato não encontrado.")
                elif contrato.status != "ativo":
                    print("Esse contrato não está ativo.")
                else:
                    contrato.finalizar()
                    print("Contrato finalizado com sucesso!")

        case "13":
            if not contratos:
                print("Cadastre um contrato primeiro.")
            else:
                print("\n===== CANCELAR CONTRATO =====")
                id = int(input("ID do contrato: "))
                contrato = contratos.get(id)

                if not contrato:
                    print("Contrato não encontrado.")
                elif contrato.status != "ativo":
                    print("Esse contrato não está ativo.")
                else:
                    contrato.cancelar()
                    print("Contrato cancelado com sucesso!")

        case "14":
            if not contratos:
                print("Cadastre um contrato primeiro.")
            else:
                id = int(input("ID do contrato que deseja excluir: "))
                contrato = contratos.get(id)

                if not contrato:
                    print("Contrato não encontrado.")
                else:
                    condutor_id = contrato.condutor_id
                    condutor = condutores.get(condutor_id)

                    del contratos[id]

                    if condutor:
                        del condutores[condutor_id]

                    print("Contrato excluído com sucesso!")
                    print("O condutor vinculado também foi excluído.")

        case "15":
            if not veiculos:
                print("Cadastre um veículo primeiro.")
            else:
                print("\n=== CADASTRO DE MANUTENÇÃO ===")
                id = gerar_id(manutencoes)
                veiculo_id = int(input("ID do veículo: "))
                veiculo = veiculos.get(veiculo_id)

                if not veiculo:
                    print("Veículo não encontrado.")
                else:
                    data = input("Data da manutenção: ")
                    tipo_servico = input("Tipo de serviço: ")
                    custo = float(input("Custo: "))

                    manutencao = Manutencao(id, veiculo_id, data, tipo_servico, custo)
                    manutencoes[id] = manutencao
                    print(f"Manutenção cadastrada com sucesso! ID: {id}")

        case "16":
            if not manutencoes:
                print("Cadastre uma manutenção primeiro.")
            else:
                print("\n==== LISTA DE MANUTENÇÕES ====")
                for manutencao in manutencoes.values():
                    print(f"\nID: {manutencao.id}")
                    print(f"Veículo ID: {manutencao.veiculo_id}")
                    print(f"Data: {manutencao.data}")
                    print(f"Serviço: {manutencao.tipo_servico}")
                    print(f"Custo: R$ {manutencao.custo:.2f}")

        case "0":
            print("Sistema encerrado.")
            break

        case _:
            print("Opção inválida.")