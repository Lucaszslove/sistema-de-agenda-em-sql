# Arquivo onde o usuário pode cadastrar os seus contatos
# tratamento de erros caso tenha dois números iguais cadastrados

from database.database import conexao, cursor, sqlite3

def cadastro_de_contato():
    try:    
        print("-- Cadastro de Contato --")
        print()
        nome = input("Digite um nome para o contato: ")
        telefone = input("Digite o número de telefone: ")
        telefone = telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")

        if nome == "" or telefone == "":
            print("Esses espaços não podem ficar vazio.")
            return
        elif not telefone.isdigit():
            print("Digite apenas números!")
        elif len(telefone) > 11 or len(telefone) < 10:
            print("Número Inválido. Comece pelo o DDD")
            return
        else:
            cursor.execute("""INSERT INTO dados_contato
                            (nome, telefone) VALUES
                            (?, ?)""", (nome, telefone))
            print("CONTATO CADASTRADO!")
            


            conexao.commit()
    except sqlite3.IntegrityError:
        print("Error: Esse telefone já está cadastrado!")

# codagem realizada, não mexer

