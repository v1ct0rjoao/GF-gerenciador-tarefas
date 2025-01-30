#criar uma lista para amarzenar as tarefas
tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print(f"tarefa '{tarefa}' adicionada com sucesso!")
    
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada")
    else:
        print("\nlista de tarefas: ")
        for i, tarefa in enumerate(tarefa,1 ):
            print(f"{i}. {tarefas}")
            
def remover_tarefas(indice):
    if 0 <= indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
    else:
        print("Indice inválido")

while True:
    print("\nGerenciador de Tarefas")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Remover Tarefa")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção")
    
    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
        adicionar_tarefa(tarefa)
    elif opcao == "2":
        listar_tarefas
    elif opcao == "3":
        listar_tarefas
        indice = int(input("Digite o número da tarefa para remover: "))
        remover_tarefas(indice)
    elif opcao == "4":
        print("Saindo do gerenciador")
        break
    else:
        print("Opção inválida! escolha uma opção de 1 a 4")

        
        