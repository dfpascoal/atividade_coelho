class Endereco:
    guardados = []

    def __init__(self, logradouro, numero, bairro, cidade, estado, cep):
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def formatar(self):
        return (
            f"{self.logradouro}, {self.numero} - {self.bairro}, "
            f"{self.cidade}/{self.estado}, CEP {self.cep}"
        )

    def atualizar(self):
        from entrada import ler_endereco

        logradouro, numero, bairro, cidade, estado, cep = ler_endereco()
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    @classmethod
    def listar(cls):
        if not cls.guardados:
            print("Nenhum endereco guardado.")
            return
        for endereco in cls.guardados:
            print(endereco.formatar())

    @classmethod
    def atualizar_guardado(cls):
        from entrada import escolher

        endereco = escolher(cls.guardados, lambda endereco: endereco.formatar())
        if endereco is None:
            return
        endereco.atualizar()
        print("Endereco atualizado.")

    @classmethod
    def remover_guardado(cls):
        from entrada import escolher

        endereco = escolher(cls.guardados, lambda endereco: endereco.formatar())
        if endereco is None:
            return
        cls.guardados.remove(endereco)
        print("Endereco removido.")
