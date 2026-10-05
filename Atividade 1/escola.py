from entrada import escolher, ler_texto
from sala_de_aula import SalaDeAula


class Escola:
    cadastrados = []

    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.salas = []        # composi??o
        self.professores = []  # associa??o

    def criar_sala(self, numero, capacidade, andar):
        sala = SalaDeAula(numero, capacidade, andar)
        self.salas.append(sala)
        return sala

    def vincular_professor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)
        if self not in professor.escolas:
            professor.escolas.append(self)

    def desvincular_professor(self, professor):
        if professor in self.professores:
            self.professores.remove(professor)
        if self in professor.escolas:
            professor.escolas.remove(self)

    def fechar(self):
        self.salas.clear()
        for professor in list(self.professores):
            self.desvincular_professor(professor)

    @classmethod
    def escolher(cls, rotulo=None):
        if rotulo is None:
            rotulo = lambda escola: f"{escola.nome} ({escola.codigo})"
        return escolher(cls.cadastrados, rotulo)

    @classmethod
    def cadastrar(cls):
        nome = ler_texto("Nome: ")
        codigo = ler_texto("Codigo: ")
        cls.cadastrados.append(cls(nome, codigo))
        print("Escola cadastrada.")

    @classmethod
    def listar(cls):
        if not cls.cadastrados:
            print("Nenhuma escola cadastrada.")
            return
        for escola in cls.cadastrados:
            print(
                f"{escola.nome} ({escola.codigo}) | "
                f"salas: {len(escola.salas)} | professores: {len(escola.professores)}"
            )

    @classmethod
    def atualizar(cls):
        escola = cls.escolher()
        if escola is None:
            return
        print("1. Nome")
        print("2. Codigo")
        opcao = input("Campo: ").strip()
        if opcao == "1":
            escola.nome = ler_texto("Novo nome: ")
        elif opcao == "2":
            escola.codigo = ler_texto("Novo codigo: ")
        else:
            print("Opcao invalida.")
            return
        print("Escola atualizada.")

    @classmethod
    def remover(cls):
        escola = cls.escolher()
        if escola is None:
            return
        escola.fechar()
        cls.cadastrados.remove(escola)
        print("Escola removida. As salas deixaram de existir. Os professores continuam cadastrados.")
