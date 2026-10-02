class Escola:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.salas = {}
        self.professores = {}

    def adicionar_sala(self, sala):
        self.salas[sala.id] = sala

    def remover_sala(self, id):
        if id in self.salas:
            del self.salas[id]

    def vincular_professor(self, professor):
        self.professores[professor.id] = professor

    def remover_professor(self, id):
        if id in self.professores:
            del self.professores[id]


class SalaDeAula:
    def __init__(self, id, nome, capacidade):
        self.id = id
        self.nome = nome
        self.capacidade = capacidade

    def alterar_capacidade(self, nova_capacidade):
        self.capacidade = nova_capacidade


class Professor:
    def __init__(self, id, nome, disciplina):
        self.id = id
        self.nome = nome
        self.disciplina = disciplina
        self.escolas = {}

    def vincular_escola(self, escola):
        self.escolas[escola.id] = escola

    def desvincular_escola(self, id):
        if id in self.escolas:
            del self.escolas[id]


class Aluno:
    def __init__(self, id, nome, matricula, endereco):
        self.id = id
        self.nome = nome
        self.matricula = matricula
        self.endereco = endereco

    def alterar_endereco(self, endereco):
        self.endereco = endereco


class Endereco:
    def __init__(self, id, rua, numero, cidade):
        self.id = id
        self.rua = rua
        self.numero = numero
        self.cidade = cidade

    def alterar_endereco(self, rua, numero, cidade):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
