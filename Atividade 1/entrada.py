def ler_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Digite algum valor.")


def ler_inteiro(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor.isdigit():
            return int(valor)
        print("Digite um numero inteiro.")


def ler_endereco():
    logradouro = ler_texto("Logradouro: ")
    numero = ler_texto("Numero: ")
    bairro = ler_texto("Bairro: ")
    cidade = ler_texto("Cidade: ")
    estado = ler_texto("Estado: ")
    cep = ler_texto("CEP: ")
    return logradouro, numero, bairro, cidade, estado, cep


def escolher(itens, rotulo):
    if not itens:
        print("Nenhum registro.")
        return None
    for indice, item in enumerate(itens, 1):
        print(f"{indice}. {rotulo(item)}")
    numero = input("Numero (0 cancela): ").strip()
    if numero == "0":
        return None
    if numero.isdigit() and 1 <= int(numero) <= len(itens):
        return itens[int(numero) - 1]
    print("Numero invalido.")
    return None
