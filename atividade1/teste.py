from ex1 import Escola, SalaDeAula, Professor, Aluno, Endereco

escolas = {}
professores = {}
alunos = {}
enderecos = {}

def gerar_id(dicionario):
    if not dicionario:
        return 1
    return max(dicionario.keys()) + 1

while True:
    print("\n========== SISTEMA ESCOLAR ==========")
    print("1 - Cadastrar escola")
    print("2 - Listar escolas")
    print("3 - Cadastrar sala")
    print("4 - Cadastrar professor")
    print("5 - Vincular professor à escola")
    print("6 - Cadastrar aluno")
    print("7 - Listar alunos")
    print("8 - Excluir escola")
    print("9 - Listar endereços")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            id = gerar_id(escolas)
            nome = input("Digite o nome da escola: ")
            escola = Escola(id, nome)
            escolas[id] = escola
            print(f"Escola cadastrada com sucesso! ID: {id}")

        case "2":
            if not escolas:
                print("Nenhuma escola cadastrada.")
            else:
                print("\n===== ESCOLAS =====")

                for escola in escolas.values():
                    print(f"ID: {escola.id}")
                    print(f"Nome: {escola.nome}")
                    print(f"Salas: {len(escola.salas)}")
                    print(f"Professores: {len(escola.professores)}")
                    print("------------------------")

        case "3":
            if not escolas:
                print("Cadastre uma escola primeiro.")
            else:
                id_escola = int(input("Digite o ID da escola: "))
                escola = escolas.get(id_escola)

                if escola is None:
                    print("Escola não encontrada.")
                else:
                    id_sala = gerar_id(escola.salas)
                    nome_sala = input("Digite o nome da sala: ")
                    capacidade = int(
                        input("Digite a capacidade da sala: ")
                    )
                    sala = SalaDeAula(
                        id_sala,
                        nome_sala,
                        capacidade
                    )
                    escola.adicionar_sala(sala)
                    print(
                        f"Sala cadastrada com sucesso! ID: {id_sala}"
                    )

        case "4":
            id = gerar_id(professores)
            nome = input("Digite o nome do professor: ")
            disciplina = input("Digite a disciplina: ")
            professor = Professor(
                id,
                nome,
                disciplina
            )
            professores[id] = professor
            print(
                f"Professor cadastrado com sucesso! ID: {id}"
            )

        case "5":
            if not professores:
                print("Nenhum professor cadastrado.")
            elif not escolas:
                print("Nenhuma escola cadastrada.")
            else:
                id_professor = int(
                    input("Digite o ID do professor: ")
                )
                id_escola = int(
                    input("Digite o ID da escola: ")
                )
                professor = professores.get(id_professor)
                escola = escolas.get(id_escola)

                if professor is None:
                    print("Professor não encontrado.")
                elif escola is None:
                    print("Escola não encontrada.")
                else:
                    escola.vincular_professor(professor)
                    professor.vincular_escola(escola)
                    print(
                        "Professor vinculado à escola com sucesso!"
                    )

        case "6":
            id = gerar_id(alunos)
            nome = input("Digite o nome do aluno: ")
            matricula = input("Digite a matrícula: ")
            print("\n===== ENDEREÇO =====")
            id_endereco = gerar_id(enderecos)
            rua = input("Digite a rua: ")
            numero = input("Digite o número: ")
            cidade = input("Digite a cidade: ")
            endereco = Endereco(
                id_endereco,
                rua,
                numero,
                cidade
            )
            enderecos[id_endereco] = endereco
            aluno = Aluno(
                id,
                nome,
                matricula,
                endereco
            )
            alunos[id] = aluno
            print(
                f"Aluno cadastrado com sucesso! ID: {id}"
            )
            print(
                f"Endereço cadastrado com sucesso! "
                f"ID: {id_endereco}"
            )

        case "7":
            if not alunos:
                print("Nenhum aluno cadastrado.")
            else:
                print("\n===== ALUNOS =====")

                for aluno in alunos.values():
                    print(f"ID: {aluno.id}")
                    print(f"Nome: {aluno.nome}")
                    print(f"Matrícula: {aluno.matricula}")
                    print(
                        f"Endereço: "
                        f"{aluno.endereco.rua}, "
                        f"{aluno.endereco.numero} - "
                        f"{aluno.endereco.cidade}"
                    )
                    print("------------------------")

        case "8":
            if not escolas:
                print("Nenhuma escola cadastrada.")
            else:
                id = int(
                    input("Digite o ID da escola: ")
                )
                escola = escolas.get(id)
                if escola is None:
                    print("Escola não encontrada.")
                else:
                    del escolas[id]
                    print(
                        "Escola excluída com sucesso!"
                    )

        case "0":
            print("Sistema encerrado, bye")
            break

        case "9":
            if not enderecos:
                print("Nenhum endereço cadastrado.")
            else:
                print("\n===== RELATÓRIO DE ENDEREÇOS =====")

                for endereco in enderecos.values():
                    print(f"ID do endereço: {endereco.id}")
                    print(f"Rua: {endereco.rua}")
                    print(f"Número: {endereco.numero}")
                    print(f"Cidade: {endereco.cidade}")

                    for aluno in alunos.values():
                        if aluno.endereco.id == endereco.id:
                            print(f"Aluno: {aluno.nome}")
                            print(f"Matrícula: {aluno.matricula}")

                    print("------------------------")
        case _:
            print("Opção inválida.")