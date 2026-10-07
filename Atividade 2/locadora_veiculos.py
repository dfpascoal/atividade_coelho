class Veiculo:
    def __init__(self, placa, modelo, ano, valor_diaria):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria

    def descrever(self):
        return f"{self.modelo} ({self.ano}) - Placa: {self.placa}"


class Condutor:
    def __init__(self, nome, numero_cnh, categoria_cnh):
        self.nome = nome
        self.numero_cnh = numero_cnh
        self.categoria_cnh = categoria_cnh

    def descrever(self):
        return f"{self.nome} (CNH: {self.numero_cnh} - Cat {self.categoria_cnh})"


class ContratoLocacao:
    def __init__(self, data_inicio, data_termino, valor_total, veiculo):
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.valor_total = valor_total
        self.status = "Ativo"
        self.veiculo = veiculo 
        self.condutor = None    

    def registrar_condutor(self, nome, numero_cnh, categoria_cnh):
        self.condutor = Condutor(nome, numero_cnh, categoria_cnh)
        return self.condutor

    def excluir_contrato(self):
        self.status = "Excluído"
        
        self.condutor = None
        
        veiculo_salvo = self.veiculo
        self.veiculo = None
        
        return veiculo_salvo

    def exibir_resumo(self):
        resumo = (
            f"=== Contrato {self.status} ===\n"
            f"Período: {self.data_inicio} até {self.data_termino} | Valor: R${self.valor_total:.2f}\n"
        )
        if self.veiculo:
            resumo += f"Veículo: {self.veiculo.descrever()}\n"
        else:
            resumo += "Veículo: Nenhum veículo vinculado\n"
            
        if self.condutor:
            resumo += f"Condutor Responsável: {self.condutor.descrever()}"
        else:
            resumo += "Condutor Responsável: Nenhum condutor registrado"
            
        return resumo


if __name__ == "__main__":
    carro = Veiculo("ABC-1234", "Chevrolet Onix", 2019, 60.00)

    contrato = ContratoLocacao("10/10/2026", "15/10/2026", 800.00, carro)

    contrato.registrar_condutor("Marcos Felix", "12345678900", "B")

    print(contrato.exibir_resumo())
    
    print("\n--- Cancelando o contrato no sistema ---\n")
    
    veiculo_liberado = contrato.excluir_contrato()
    
    print(contrato.exibir_resumo())
    
    print(f"\nO veículo ainda existe na memória? Sim: {veiculo_liberado.descrever()}")