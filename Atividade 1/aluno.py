from endereco import Endereco


class Aluno:
    cadastrados = []

    def __init__(self, nome, matricula, logradouro, numero, bairro, cidade, estado, cep):
        self.nome = nome
        self.matricula = matricula
        self.endereco = Endereco(logradouro, numero, bairro, cidade, estado, cep)  # agregaç?o

    def texto(self):
        if self.endereco is None:
            return f"{self.nome} ({self.matricula}) - sem endereco"
        return f"{self.nome} ({self.matricula}) - {self.endereco.formatar()}"

    def desvincular_endereco(self):
        endereco = self.endereco
        self.endereco = None
        return endereco

    @classmethod
    def cadastrar(cls):
        from entrada import ler_endereco, ler_texto

        nome = ler_texto("Nome: ")
        matricula = ler_texto("Matricula: ")
        dados = ler_endereco()
        cls.cadastrados.append(cls(nome, matricula, *dados))
        print("Aluno cadastrado com endereco.")

    @classmethod
    def listar(cls):
        if not cls.cadastrados:
            print("Nenhum aluno cadastrado.")
            return
        for aluno in cls.cadastrados:
            print(aluno.texto())

    @classmethod
    def atualizar(cls):
        from entrada import escolher, ler_texto

        aluno = escolher(cls.cadastrados, lambda aluno: aluno.texto())
        if aluno is None:
            return
        print("1. Nome")
        print("2. Matricula")
        print("3. Endereco")
        opcao = input("Campo: ").strip()
        if opcao == "1":
            aluno.nome = ler_texto("Novo nome: ")
        elif opcao == "2":
            aluno.matricula = ler_texto("Nova matricula: ")
        elif opcao == "3":
            if aluno.endereco is None:
                print("Este aluno nao tem endereco.")
                return
            aluno.endereco.atualizar()
        else:
            print("Opcao invalida.")
            return
        print("Aluno atualizado.")

    @classmethod
    def remover(cls):
        from entrada import escolher

        aluno = escolher(cls.cadastrados, lambda aluno: aluno.texto())
        if aluno is None:
            return
        endereco = aluno.desvincular_endereco()
        if endereco is not None:
            Endereco.guardados.append(endereco)
        cls.cadastrados.remove(aluno)
        print("Aluno removido. O endereco foi guardado no menu de enderecos.")
