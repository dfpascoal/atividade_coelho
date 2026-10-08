# Atividade 2 — Locadora de Veículos

**Componentes:** Artênio Felix, David Fernando, David Lucas, Luis Claudio, Luis Gabriel, Rafael Araújo

**Estudo de Caso:** Sistema de Gerenciamento de uma Locadora de Veículos

## 1. Identificação de classes

**Veículo:** A classe Veículo representa os veículos disponíveis para locação. Alguns atributos podem ser `placa`, `modelo`, `ano` e `valor_diaria`. Como métodos, podemos ter `verificar_disponibilidade()` e `calcular_valor_diaria()`, utilizados para controlar a disponibilidade e o valor da locação.

**Carro:** A classe Carro representa os veículos do tipo carro. Seus atributos podem ser quantidade de portas, tipo de combustível e possui ar-condicionado. Como métodos, podemos ter `abrir_portas()` e `calcular_valor_diaria()`.

**Moto:** A classe Moto representa os veículos do tipo motocicleta. Seus atributos podem ser cilindradas, tipo de motor e possui baú. Como métodos, podemos ter `ligar_motor()` e `calcular_valor_diaria()`.

**Caminhão:** A classe Caminhão representa os veículos utilizados para transporte de cargas. Seus atributos podem ser capacidade de carga, quantidade de eixos e tipo de carroceria. Como métodos, podemos ter `carregar_carga()` e `calcular_valor_diaria()`.

**Cliente:** A classe Cliente representa os clientes da locadora. Seus atributos podem ser nome ou razão social, documento e telefone. Como métodos, podemos ter `atualizar_telefone()` e `consultar_contratos()`.

**Pessoa Física:** A classe Pessoa Física representa os clientes que são pessoas físicas. Seus atributos podem ser CPF, data de nascimento e endereço. Como métodos, podemos ter `validar_cpf()` e `atualizar_endereco()`.

**Pessoa Jurídica:** A classe Pessoa Jurídica representa os clientes que são empresas. Seus atributos podem ser CNPJ, razão social e nome fantasia. Como métodos, podemos ter `validar_cnpj()` e `atualizar_dados_empresa()`.

**Contrato de Locação:** A classe Contrato de Locação representa o aluguel realizado entre um cliente e um veículo. Seus atributos podem ser data de início, data de término prevista, valor total e status. Como métodos, podemos ter `finalizar_contrato()` e `cancelar_contrato()`.

**Condutor:** A classe Condutor representa a pessoa responsável por conduzir o veículo durante a locação. Seus atributos podem ser nome, número da CNH e categoria da CNH. Como métodos, podemos ter `validar_cnh()` e `atualizar_cnh()`.

**Manutenção:** A classe Manutenção representa os serviços realizados nos veículos. Seus atributos podem ser data, tipo de serviço e custo. Como métodos, podemos ter `registrar_manutencao()` e `calcular_custo()`.

## 2. Herança

O cenário apresenta duas hierarquias de generalização e especialização.

- **Veículo → Carro, Moto e Caminhão — Herança:** A classe Veículo funciona como superclasse, pois possui informações comuns a todos os veículos, como placa, modelo, ano e valor da diária. Carro, Moto e Caminhão são subclasses porque representam tipos específicos de veículos e possuem características próprias.
- **Cliente → Pessoa Física e Pessoa Jurídica — Herança:** A classe Cliente funciona como superclasse, pois representa as informações comuns aos clientes da locadora. Pessoa Física e Pessoa Jurídica são subclasses, pois representam tipos diferentes de clientes, sendo identificados por CPF e CNPJ, respectivamente.

**Resumindo:** Veículo → Carro, Moto e Caminhão = Herança (especialização dos tipos de veículos); Cliente → Pessoa Física e Pessoa Jurídica = Herança (especialização dos tipos de clientes).

## 3. Relacionamentos entre classes

- **Cliente → Contrato de Locação — Associação:** O cliente está relacionado aos contratos de locação que realiza. Um cliente pode possuir vários contratos, mas pode continuar existindo no sistema mesmo que seus contratos sejam finalizados ou excluídos.
- **Veículo → Contrato de Locação — Associação:** O contrato está vinculado a um veículo específico. O veículo, porém, pode continuar existindo após o término do contrato e pode ser utilizado em uma nova locação.
- **Contrato de Locação → Condutor — Composição:** O condutor está diretamente relacionado ao contrato de locação. De acordo com o cenário, o condutor só existe associado a um contrato e, caso o contrato seja excluído, os dados do condutor não possuem mais motivo para existir isoladamente no sistema. Por isso, existe uma dependência forte entre as duas classes.
- **Veículo → Manutenção — Composição:** A manutenção pertence a um veículo específico e faz parte do histórico de manutenção desse veículo. Caso o veículo deixe de existir no sistema, as manutenções associadas a ele também deixam de ter sentido como registros independentes.
- **Veículo → Carro — Herança:** Carro é um tipo específico de Veículo e herda suas características e comportamentos.
- **Veículo → Moto — Herança:** Moto é um tipo específico de Veículo e herda suas características e comportamentos.
- **Veículo → Caminhão — Herança:** Caminhão é um tipo específico de Veículo e herda suas características e comportamentos.
- **Cliente → Pessoa Física — Herança:** Pessoa Física é um tipo específico de Cliente e possui características próprias, como CPF.
- **Cliente → Pessoa Jurídica — Herança:** Pessoa Jurídica é um tipo específico de Cliente e possui características próprias, como CNPJ.

**Resumindo:**

| Relação | Tipo |
|---|---|
| Cliente e Contrato de Locação | Associação |
| Veículo e Contrato de Locação | Associação |
| Contrato de Locação e Condutor | Composição (dependência forte) |
| Veículo e Manutenção | Composição (dependência forte) |
| Veículo e seus tipos | Herança |
| Cliente e seus tipos | Herança |

## 4. Implementação parcial

Para a implementação parcial, foram escolhidas as classes Contrato de Locação e Condutor, que possuem uma relação de composição. Nessa relação, o contrato possui um condutor responsável pela locação. O condutor é criado e associado ao contrato, não possuindo existência independente dentro do sistema de acordo com as regras apresentadas no cenário.

A implementação em Python, no arquivo [`locadora_veiculos.py`](locadora_veiculos.py), demonstra que a classe `ContratoLocacao` instancia a classe `Condutor`, estabelecendo a relação de composição entre as duas classes:

- **Composição:** `registrar_condutor()` cria o `Condutor` dentro do próprio contrato. Quando o contrato é excluído (`excluir_contrato()`), o condutor é descartado junto.
- **Associação:** o `Veiculo` é criado fora do contrato e apenas passado para ele. Ao excluir o contrato, o veículo é desvinculado, mas continua existindo e pode ser usado em uma nova locação.

### Como executar

```bash
python locadora_veiculos.py
```

Saída:

```
=== Contrato Ativo ===
Período: 10/10/2026 até 15/10/2026 | Valor: R$800.00
Veículo: Chevrolet Onix (2019) - Placa: ABC-1234
Condutor Responsável: Marcos Felix (CNH: 12345678900 - Cat B)

--- Cancelando o contrato no sistema ---

=== Contrato Excluído ===
Período: 10/10/2026 até 15/10/2026 | Valor: R$800.00
Veículo: Nenhum veículo vinculado
Condutor Responsável: Nenhum condutor registrado

O veículo ainda existe na memória? Sim: Chevrolet Onix (2019) - Placa: ABC-1234
```
