class Endereco:
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


class Aluno:
    def __init__(self, nome, matricula, endereco):
        self.nome = nome
        self.matricula = matricula
        self.endereco = endereco  # agregação

    def desvincular_endereco(self):
        endereco = self.endereco
        self.endereco = None
        return endereco


class Professor:
    def __init__(self, nome, registro, formacao):
        self.nome = nome
        self.registro = registro
        self.formacao = formacao
        self.escolas = []  # associação

    def listar_escolas(self):
        return [escola.nome for escola in self.escolas]


class SalaDeAula:
    def __init__(self, numero, capacidade, andar):
        self.numero = numero
        self.capacidade = capacidade
        self.andar = andar

    def descrever(self):
        return f"Sala {self.numero}, andar {self.andar}, capacidade {self.capacidade}"


class Escola:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.salas = []        # composição
        self.professores = []  # associação

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


if __name__ == "__main__":
    escola_a = Escola("Escola Municipal Norte", "EMN-01")
    escola_b = Escola("Colegio Estadual Sul", "CES-02")

    sala = escola_a.criar_sala("101", 30, 1)
    escola_a.criar_sala("202", 25, 2)

    professora = Professor("Ana Lima", "PRF-100", "Licenciatura em Matematica")
    escola_a.vincular_professor(professora)
    escola_b.vincular_professor(professora)

    endereco = Endereco("Rua das Flores", "120", "Centro", "Recife", "PE", "50000-000")
    aluno = Aluno("Bruno Souza", "2026001", endereco)

    print(sala.descrever())
    print(professora.listar_escolas())
    print(endereco.formatar())

    endereco_salvo = aluno.desvincular_endereco()
    escola_a.fechar()

    print("Salas depois de fechar:", escola_a.salas)
    print("Escolas da professora:", professora.listar_escolas())
    print("Endereco ainda existe:", endereco_salvo.formatar())
