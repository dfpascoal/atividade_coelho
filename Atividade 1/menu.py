from aluno import Aluno
from endereco import Endereco
from escola import Escola
from professor import Professor
from sala_de_aula import SalaDeAula


def menu_escolas():
    while True:
        print("\n--- ESCOLAS ---")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Remover")
        print("0. Voltar")
        opcao = input("Opcao: ").strip()
        if opcao == "1":
            Escola.cadastrar()
        elif opcao == "2":
            Escola.listar()
        elif opcao == "3":
            Escola.atualizar()
        elif opcao == "4":
            Escola.remover()
        elif opcao == "0":
            return
        else:
            print("Opcao invalida.")


def menu_salas():
    while True:
        print("\n--- SALAS ---")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Remover")
        print("0. Voltar")
        opcao = input("Opcao: ").strip()
        if opcao == "1":
            SalaDeAula.cadastrar()
        elif opcao == "2":
            SalaDeAula.listar()
        elif opcao == "3":
            SalaDeAula.atualizar()
        elif opcao == "4":
            SalaDeAula.remover()
        elif opcao == "0":
            return
        else:
            print("Opcao invalida.")


def menu_professores():
    while True:
        print("\n--- PROFESSORES ---")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Remover")
        print("5. Vincular a uma escola")
        print("6. Desvincular de uma escola")
        print("0. Voltar")
        opcao = input("Opcao: ").strip()
        if opcao == "1":
            Professor.cadastrar()
        elif opcao == "2":
            Professor.listar()
        elif opcao == "3":
            Professor.atualizar()
        elif opcao == "4":
            Professor.remover()
        elif opcao == "5":
            Professor.vincular()
        elif opcao == "6":
            Professor.desvincular()
        elif opcao == "0":
            return
        else:
            print("Opcao invalida.")


def menu_alunos():
    while True:
        print("\n--- ALUNOS ---")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Remover")
        print("0. Voltar")
        opcao = input("Opcao: ").strip()
        if opcao == "1":
            Aluno.cadastrar()
        elif opcao == "2":
            Aluno.listar()
        elif opcao == "3":
            Aluno.atualizar()
        elif opcao == "4":
            Aluno.remover()
        elif opcao == "0":
            return
        else:
            print("Opcao invalida.")


def menu_enderecos():
    while True:
        print("\n--- ENDERECOS GUARDADOS ---")
        print("Eles continuam aqui depois que o aluno e removido.")
        print("1. Listar")
        print("2. Atualizar")
        print("3. Remover")
        print("0. Voltar")
        opcao = input("Opcao: ").strip()
        if opcao == "1":
            Endereco.listar()
        elif opcao == "2":
            Endereco.atualizar_guardado()
        elif opcao == "3":
            Endereco.remover_guardado()
        elif opcao == "0":
            return
        else:
            print("Opcao invalida.")


def menu_principal():
    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Escolas")
        print("2. Salas")
        print("3. Professores")
        print("4. Alunos")
        print("5. Enderecos guardados")
        print("0. Sair")
        opcao = input("Opcao: ").strip()
        if opcao == "1":
            menu_escolas()
        elif opcao == "2":
            menu_salas()
        elif opcao == "3":
            menu_professores()
        elif opcao == "4":
            menu_alunos()
        elif opcao == "5":
            menu_enderecos()
        elif opcao == "0":
            print("Ate logo.")
            return
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    menu_principal()
