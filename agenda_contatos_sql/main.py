# Menu incial do programa de agendas de contatos utilizando sqlite3
from modules.agenda import agenda # importando a função agenda
from modules.buscar_contato import buscar_contato # importando a função buscar os contatos
from modules.cadastro_de_contatos import cadastro_de_contato # importando a função cadastrar os contatos
from modules.excluir_contato import excluir_contato # importando a função excluir contato

while True:
    try:
        print("--- Sistema de Agenda de Contatos ---")
        print()
        print("""[1] Cadastrar Contatos
[2] Acessar Agenda
[3] Atualizar Contato
[4] Excluir Contato
[5] Sair""")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            cadastro_de_contato() # Cadastrar contatos
        elif opcao == 2:
            agenda() # Listar os contatos cadastrados
        elif opcao == 3:
            buscar_contato() # Buscar contatos para fazer atualização
        elif opcao == 4:
            excluir_contato()
        elif opcao == 5:
            print("Você Saiu!")
            break
        else:
            print("Digite apenas as opções de [1] a [5]")
            continue
    except ValueError:
        print("Digite apenas números!!")
        continue