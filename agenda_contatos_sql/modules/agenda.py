# Página de contato, onde o usuário pode ver todos os seus contatos listados
# Pode ver por id, nome e telefone
# telefone formatado para mostrar (99) 99999-9999

from database.database import conexao, cursor

def agenda():
    cursor.execute("""SELECT id, nome, telefone FROM dados_contato""")
    agenda = cursor.fetchall()
    if not agenda:
        print("Nenhum contato registrado no momento.")
    else:
        for c in agenda:
            id, nome, telefone = c
            print(f"""Id: {id}
Nome: {nome}
Telefone: ({telefone[:2]}) {telefone[2:7]}-{telefone[7:11]}""")
            print()
    
        conexao.commit()
        return True
# Codagem realizada, não mexer

