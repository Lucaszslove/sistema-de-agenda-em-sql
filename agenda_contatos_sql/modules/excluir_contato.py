
from database.database import conexao, cursor
from modules.agenda import agenda

def excluir_contato():
    try:
        print("--- Remover Contato ---")
        contatos = agenda()
        if not contatos:
            return

        escolha_id = int(input("Digite o ID do contato que você deseja remover: "))
        cursor.execute("""SELECT id FROM dados_contato
                       WHERE id = ?""", (escolha_id,))

        contato = cursor.fetchone()
        if contato is None:
            print("Contato não encontrado...")
            return
        else:
            cursor.execute("""DELETE FROM dados_contato
                        WHERE id = ?""", (escolha_id,))
            print("CONTATO REMOVIDO COM SUCESSO!")
            conexao.commit()
    except ValueError:
        print("Digite apenas números...")
        return






