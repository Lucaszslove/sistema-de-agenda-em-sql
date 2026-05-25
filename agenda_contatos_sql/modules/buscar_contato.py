# Essa é a parte onde o usuário pode atualizar o contato, seja nome ou
# número de telefone

from database.database import conexao, cursor

def buscar_contato():
    try:
        print("-- Buscar Contato --")
        print()
        buscar_id = input("Digite o ID do contato que você deseja buscar: ")
        
        if not buscar_id.isdigit():
            print("Digite apenas números...")
            return
        
        cursor.execute("""SELECT id, nome, telefone FROM dados_contato
                    WHERE id = ?""", (buscar_id,))
        
        contato = cursor.fetchone()

        if contato is None:
            print("Contato não encontrado...")
            return
        else:
            id, nome, telefone = contato
            print(f"""Id: {id}
Nome: {nome}
Telefone: {telefone}""")
        escolha = input("Deseja atualizar o contato?\n[S] Sim ou [N] Não: ").lower()
        if escolha == "s":
            print("Escolha umas das opções para atualizar o contato:")
            print()
            print("[1] Atualizar nome\n[2] Atualizar número\n[3] Sair")
            opcao = int(input("Digite a opção: "))
            if opcao == 1:
                nome_atualizado = input("Digite um novo nome: ")
                cursor.execute("""UPDATE dados_contato
                            SET nome = ?""", (nome_atualizado,))
                conexao.commit()
                print("NOME ATUALIZADO!")
                return
            elif opcao == 2:
                numero_atualizado = input("Digite o novo número: ")
                if len(numero_atualizado) > 11 or len(numero_atualizado) < 10:
                    print("Número Inválido! Comece pelo o DDD")
                    return
                else:
                    cursor.execute("""UPDATE dados_contato SET telefone = ?""", (numero_atualizado,))
                    conexao.commit()
                    print("TELEFONE ATUALIZADO!")
                    return
            elif opcao == 3:
                return
            else:
                print("Escolha apenas as opções de [1] a [3]")
        elif escolha == "n":
            return
        elif len(escolha) > 1:
            print("Digite apenas [S] ou [N]")
        elif escolha.isalpha():
            print("Digite apenas letras")
        
        conexao.commit()
    except ValueError:
        print("Digite apenas números!")
        return