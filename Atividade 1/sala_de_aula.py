class SalaDeAula:
    def __init__(self, numero, capacidade, andar):
        self.numero = numero
        self.capacidade = capacidade
        self.andar = andar

    def descrever(self):
        return f"Sala {self.numero}, andar {self.andar}, capacidade {self.capacidade}"

    def atualizar_dados(self):
        from entrada import ler_inteiro, ler_texto

        print("1. Numero")
        print("2. Capacidade")
        print("3. Andar")
        opcao = input("Campo: ").strip()
        if opcao == "1":
            self.numero = ler_texto("Novo numero: ")
        elif opcao == "2":
            self.capacidade = ler_inteiro("Nova capacidade: ")
        elif opcao == "3":
            self.andar = ler_inteiro("Novo andar: ")
        else:
            print("Opcao invalida.")
            return
        print("Sala atualizada.")

    @classmethod
    def cadastrar(cls):
        from entrada import ler_inteiro, ler_texto
        from escola import Escola

        escola = Escola.escolher(lambda escola: escola.nome)
        if escola is None:
            return
        numero = ler_texto("Numero da sala: ")
        capacidade = ler_inteiro("Capacidade: ")
        andar = ler_inteiro("Andar: ")
        escola.criar_sala(numero, capacidade, andar)
        print("Sala cadastrada.")

    @classmethod
    def listar(cls):
        from escola import Escola

        if not Escola.cadastrados:
            print("Nenhuma escola cadastrada.")
            return
        for escola in Escola.cadastrados:
            print(f"\n{escola.nome}")
            if not escola.salas:
                print("  Sem salas.")
            for sala in escola.salas:
                print(f"  {sala.descrever()}")

    @classmethod
    def atualizar(cls):
        from entrada import escolher
        from escola import Escola

        escola = Escola.escolher(lambda escola: escola.nome)
        if escola is None:
            return
        sala = escolher(escola.salas, lambda sala: sala.descrever())
        if sala is None:
            return
        sala.atualizar_dados()

    @classmethod
    def remover(cls):
        from entrada import escolher
        from escola import Escola

        escola = Escola.escolher(lambda escola: escola.nome)
        if escola is None:
            return
        sala = escolher(escola.salas, lambda sala: sala.descrever())
        if sala is None:
            return
        escola.salas.remove(sala)
        print("Sala removida.")
