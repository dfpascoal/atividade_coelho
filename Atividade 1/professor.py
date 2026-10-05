class Professor:
    cadastrados = []

    def __init__(self, nome, registro, formacao):
        self.nome = nome
        self.registro = registro
        self.formacao = formacao
        self.escolas = []  # associa??o

    def listar_escolas(self):
        return [escola.nome for escola in self.escolas]

    def texto(self):
        nomes = ", ".join(self.listar_escolas()) or "nenhuma escola"
        return f"{self.nome} ({self.registro}) - {self.formacao} | {nomes}"

    @classmethod
    def cadastrar(cls):
        from entrada import ler_texto

        nome = ler_texto("Nome: ")
        registro = ler_texto("Registro: ")
        formacao = ler_texto("Formacao: ")
        cls.cadastrados.append(cls(nome, registro, formacao))
        print("Professor cadastrado.")

    @classmethod
    def listar(cls):
        if not cls.cadastrados:
            print("Nenhum professor cadastrado.")
            return
        for professor in cls.cadastrados:
            print(professor.texto())

    @classmethod
    def atualizar(cls):
        from entrada import escolher, ler_texto

        professor = escolher(cls.cadastrados, lambda professor: professor.texto())
        if professor is None:
            return
        print("1. Nome")
        print("2. Registro")
        print("3. Formacao")
        opcao = input("Campo: ").strip()
        if opcao == "1":
            professor.nome = ler_texto("Novo nome: ")
        elif opcao == "2":
            professor.registro = ler_texto("Novo registro: ")
        elif opcao == "3":
            professor.formacao = ler_texto("Nova formacao: ")
        else:
            print("Opcao invalida.")
            return
        print("Professor atualizado.")

    @classmethod
    def remover(cls):
        from entrada import escolher

        professor = escolher(cls.cadastrados, lambda professor: professor.texto())
        if professor is None:
            return
        for escola in list(professor.escolas):
            escola.desvincular_professor(professor)
        cls.cadastrados.remove(professor)
        print("Professor removido. As escolas continuam cadastradas.")

    @classmethod
    def vincular(cls):
        from entrada import escolher
        from escola import Escola

        professor = escolher(cls.cadastrados, lambda professor: professor.texto())
        if professor is None:
            return
        escola = Escola.escolher(lambda escola: escola.nome)
        if escola is None:
            return
        escola.vincular_professor(professor)
        print("Professor vinculado.")

    @classmethod
    def desvincular(cls):
        from entrada import escolher

        professor = escolher(cls.cadastrados, lambda professor: professor.texto())
        if professor is None:
            return
        escola = escolher(professor.escolas, lambda escola: escola.nome)
        if escola is None:
            return
        escola.desvincular_professor(professor)
        print("Professor desvinculado.")
