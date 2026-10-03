from datetime import datetime

class Veiculo:
    def __init__(self, placa, modelo, ano, valor_diaria):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria

    def calcular_diaria(self, quantidade_dias):
        return self.valor_diaria * quantidade_dias

    def alterar_valor_diaria(self, novo_valor):
        self.valor_diaria = novo_valor

class Carro(Veiculo):
    def __init__(self, id, quantidade_portas, cambio, placa, modelo, ano, valor_diaria):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.id = id
        self.quantidade_portas = quantidade_portas
        self.cambio = cambio

    def contar_portas(self):
        return self.quantidade_portas

    def mostrar_cambio(self):
        return self.cambio

class Moto(Veiculo):
    def __init__(self, id, cilindradas, partida, placa, modelo, ano, valor_diaria):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.id = id
        self.cilindradas = cilindradas
        self.partida = partida

    def mostrar_cilindradas(self):
        return self.cilindradas

    def saber_partida(self):
        return self.partida

class Caminhao(Veiculo):
    def __init__(self, id, quantidade_carga, quantidade_eixos, placa, modelo, ano, valor_diaria):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.id = id
        self.quantidade_carga = quantidade_carga
        self.quantidade_eixos = quantidade_eixos

    def contar_eixos(self):
        return self.quantidade_eixos

    def disponibilidade_carga(self):
        return self.quantidade_carga

class Cliente:
    def __init__(self, nome, razao_social, documento, telefone):
        self.nome = nome
        self.razao_social = razao_social
        self.documento = documento
        self.telefone = telefone

    def atualizar_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    def atualizar_documento(self, novo_documento):
        self.documento = novo_documento

class Fisica(Cliente):
    def __init__(self, id, nome, razao_social, documento, telefone):
        super().__init__(nome, razao_social, documento, telefone)
        self.id = id

    def atualizar_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    def validar_documentos(self):
        return len(self.documento) == 11

class Juridica(Cliente):
    def __init__(self, id, nome, razao_social, documento, telefone):
        super().__init__(nome, razao_social, documento, telefone)
        self.id = id
        
    def atualizar_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    def validar_documentos(self):
        return len(self.documento) == 14

class Contrato:
    def __init__(self, id, data_inicio, data_termino, valor_total, status, cliente_id, veiculo_id, condutor_id):
        self.id = id
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.valor_total = valor_total
        self.status = status
        self.cliente_id = cliente_id
        self.veiculo_id = veiculo_id
        self.condutor_id = condutor_id

    def calcular_valor_total(self, valor_diaria):
        inicio = datetime.strptime(self.data_inicio, "%d/%m/%Y")
        termino = datetime.strptime(self.data_termino, "%d/%m/%Y")
        dias = (termino - inicio).days
        self.valor_total = dias * valor_diaria
        return self.valor_total

    def finalizar(self):
        self.status = "finalizado"

    def cancelar(self):
        self.status = "cancelado"

class Condutor:
    def __init__(self, id, nome, cnh, contrato_id=None):
        self.id = id
        self.nome = nome
        self.cnh = cnh
        self.contrato_id = contrato_id

    def atualizar_cnh(self, nova_cnh):
        self.cnh = nova_cnh

    def atualizar_nome(self, novo_nome):
        self.nome = novo_nome

class Manutencao:
    def __init__(self, id, veiculo_id, data, tipo_servico, custo):
        self.id = id
        self.veiculo_id = veiculo_id
        self.data = data
        self.tipo_servico = tipo_servico
        self.custo = custo

    def alterar_custo(self, novo_custo):
        self.custo = novo_custo

    def alterar_servico(self, novo_servico):
        self.tipo_servico = novo_servico