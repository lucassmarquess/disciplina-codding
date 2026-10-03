# Para demonstrar a composição, podemos utilizar Contrato e Condutor.
# O contrato recebe o ID do condutor responsável no momento da sua criação:

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

# Na criação do contrato, o sistema recebe o condutor:

condutor_id = int(input("ID do condutor: "))
condutor = condutores.get(condutor_id)

contrato = Contrato(id, data_inicio, data_termino, 0, "ativo", cliente_id, veiculo_id, condutor_id)
contratos[id] = contrato

# Quando o contrato é excluído, o condutor associado também é removido:

condutor_id = contrato.condutor_id
condutor = condutores.get(condutor_id)

del contratos[id]

if condutor:
    del condutores[condutor_id]

# Dessa forma, a implementação demonstra a composição, pois o Condutor está diretamente relacionado ao Contrato e seu registro é eliminado quando o contrato correspondente é excluído.