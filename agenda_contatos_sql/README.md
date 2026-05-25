# Agenda de Contatos com SQLite

Projeto de agenda de contatos desenvolvido em Python, utilizando SQLite para armazenar os dados cadastrados.

O sistema roda pelo terminal e permite cadastrar, listar, buscar, atualizar e excluir contatos.

## Funcionalidades

- Cadastrar contatos com nome e telefone
- Listar todos os contatos cadastrados
- Buscar contato pelo ID
- Atualizar nome ou telefone de um contato
- Excluir contato pelo ID
- Validar campos vazios
- Validar telefone com DDD
- Evitar cadastro de telefones duplicados
- Criar automaticamente o banco de dados e a tabela, caso ainda não existam

## Tecnologias utilizadas

- Python
- SQLite
- Módulo `sqlite3`

## Estrutura do projeto

```text
agenda_contatos_sql/
├── database/
│   └── database.py
├── imagens/
│   ├── cadastro_contato.jpg
│   └── interface_programa.jpg
├── modules/
│   ├── agenda.py
│   ├── buscar_contato.py
│   ├── cadastro_de_contatos.py
│   └── excluir_contato.py
├── main.py
└── README.md
```

## Como executar

1. Clone o repositório:

```bash
git clone https://github.com/Lucaszslove/sistema-de-agenda-em-sql
```

2. Acesse a pasta do projeto:

```bash
cd agenda_contatos_sql
```

3. Execute o arquivo principal:

```bash
python3 main.py
```

## Menu do sistema

Ao executar o projeto, será exibido um menu no terminal:

```text
[1] Cadastrar Contatos
[2] Acessar Agenda
[3] Atualizar Contato
[4] Excluir Contato
[5] Sair
```

## Banco de dados

O projeto utiliza um banco SQLite chamado `database.db`.

A tabela principal é criada automaticamente com a seguinte estrutura:

```sql
CREATE TABLE IF NOT EXISTS dados_contato(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL UNIQUE
);
```

## Imagens

### Interface do programa

![Interface do programa](imagens/interface_programa.jpg)

### Cadastro de contato

![Cadastro de contato](imagens/cadastro_contato.jpg)

## Observação

O arquivo `database.db` é gerado automaticamente durante a execução do programa e não precisa ser enviado para o repositório.
