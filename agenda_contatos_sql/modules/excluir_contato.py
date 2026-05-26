
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

            cursor.execute("SELECT COUNT(*) FROM dados_contato")
            quantidade = cursor.fetchone()[0]

            if quantidade == 0:
                cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'dados_contato'")

            print("CONTATO REMOVIDO COM SUCESSO!")
            
            conexao.commit()
    except ValueError:
        print("Digite apenas números...")
        return






