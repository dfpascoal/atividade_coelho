# Atividade 1 — Sistema Escolar

**Componentes:** Artênio Félix, David Fernando, David Lucas, Luís Claudio, Luís Gabriel, Rafael Araújo

## 1. Entidades, atributos e métodos

**Escola:** A classe Escola representa a instituição de ensino. Alguns atributos poderiam ser `nome`, `cnpj`, `endereco` e `telefone`. Como métodos, podemos ter `adicionar_sala()`, `remover_sala()` e `adicionar_professor()`, que servem para gerenciar as informações relacionadas à escola.

**Sala de Aula:** A classe Sala de Aula representa os espaços físicos da escola. Seus atributos podem ser `numero`, `capacidade` e `andar`. Entre os métodos, podemos ter `reservar()` e `liberar()`, para controlar a utilização da sala.

**Professor:** A classe Professor representa os professores que podem trabalhar em uma ou mais escolas. Alguns atributos seriam `nome`, `cpf`, `email` e `especialidade`. Como métodos, podemos ter `lecionar()` e `adicionar_escola()`, permitindo relacionar o professor às escolas onde ele trabalha.

**Aluno:** A classe Aluno representa os estudantes cadastrados. Seus atributos podem ser `nome`, `matricula`, `email` e `curso`. Como métodos, podemos ter `matricular()` e `atualizar_endereco()`.

**Endereço:** A classe Endereço representa o endereço de um aluno. Seus atributos podem ser `rua`, `numero`, `bairro`, `cidade` e `cep`. Um método possível seria `atualizar()`, utilizado para alterar os dados do endereço.

## 2. Classificação das relações

- **Escola → Sala de Aula — Composição:** A sala depende da escola para existir no sistema. Se a escola for removida, as salas também deixam de existir.
- **Escola ↔ Professor — Associação:** Professor e escola podem existir separadamente. Um professor pode trabalhar em várias escolas e uma escola pode ter vários professores.
- **Aluno → Endereço — Agregação:** O endereço é criado junto com o aluno e está relacionado a ele, mas pode continuar existindo mesmo depois que o aluno for removido.

**Resumindo:**

| Relação | Tipo | Dependência |
|---|---|---|
| Escola e Sala de Aula | Composição | Forte: a sala não existe sem a escola |
| Escola e Professor | Associação | Nenhuma dependência de existência |
| Aluno e Endereço | Agregação | O endereço pode continuar existindo separadamente |

## 3. Diagrama de Classe

![Diagrama de classes do sistema escolar](diagrama_classes.svg)

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `escola.py` | Classe `Escola` |
| `sala_de_aula.py` | Classe `SalaDeAula` |
| `professor.py` | Classe `Professor` |
| `aluno.py` | Classe `Aluno` |
| `endereco.py` | Classe `Endereco` |
| `entrada.py` | Funções de leitura de dados do usuário |
| `menu.py` | Menu principal do sistema |
| `sistema_escolar.py` | Versão em arquivo único com todas as classes e um exemplo de uso |
| `diagrama_classes.svg` | Diagrama de classes |
