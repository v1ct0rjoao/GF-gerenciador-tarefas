import os #biblioteca para lidar com arquivos

ARQUIVO_TAREFAS = "C:/Users/joaov\Documents/Programação/Python/GF-gerenciador-tarefas/tarefas.txt"

def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r") as file:
            return[linha.strip() for linha in file.readlines()]
    return []
    
def salvar_tarefas():
    with open(ARQUIVO_TAREFAS, "w") as file:
        for tarefa in tarefas:
            file.write(tarefa + "\n")
            
tarefas =  carregar_tarefas()

def adicionar_tarefas(tarefa):
    tarefas.append(tarefa)
    salvar_tarefas()
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")
    
def listar_tarefas():
    salvar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa cadastrada")
    else:
        print("\n Lista de Tarefas")
        for i, tarefa in enumerate(tarefas,1):
            print(f"{i}. {tarefa}")
            
def remover_tarefas(indice):
    if 0 <= indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        salvar_tarefas()
        print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
    else:
        print("indice inválido")

while True:
    print("\nGerenciador de Tarefas")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Remover Tarefa")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
        adicionar_tarefas(tarefa)
        
    elif opcao == "2":
        listar_tarefas()
        
    elif opcao == "3":
        listar_tarefas()
        try:
            indice = int(input("Digite o número da tarefa para remover: ")) - 1
            remover_tarefas(indice)
            
        except ValueError:
            print("Por favor, insira um número válido!")
            
            
    elif opcao == "4":
        print("Saindo do gerenciador. Até mais!")
        break
    else:
        print("Opção inválida! Escolha uma opção de 1 a 4.")