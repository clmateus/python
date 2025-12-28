# %%
NOME_FICHEIRO = "tarefas.txt"

def carregar_tarefas():
    lista = []
    try:
        with open(NOME_FICHEIRO, "r", encoding='utf-8') as arquivo:
            lista = [linha.strip() for linha in arquivo.readlines()]
    except FileNotFoundError:
        # Se o ficheiro não existir, retorna lista vazia sem dar erro
        pass
    return lista

def salvar_tarefas(lista):
    with open(NOME_FICHEIRO, "w", encoding='utf-8') as arquivo:
        for tarefa in lista:
            arquivo.write(f"{tarefa}\n")

def mostrar_menu():
    print("\n" + "="*30)
    print("      TASK MASTER 1.0")
    print("="*30)
    print("1. Nova Tarefa")
    print("2. Ver Tarefas")
    print("3. Concluir/Remover Tarefa")
    print("4. Sair")

tarefas = carregar_tarefas()

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nova = input("Digite a tarefa: ")
        tarefas.append(nova)
        salvar_tarefas(tarefas)
        print("✅ Tarefa adicionada!")

    elif opcao == "2":
        print("\n--- SUAS TAREFAS ---")
        if not tarefas:
            print("Nenhuma tarefa pendente.")
        else:
            # enumerate ajuda a mostrar o índice (começando do 1 para o utilizador)
            for i, item in enumerate(tarefas, 1):
                print(f"{i}. {item}")

    elif opcao == "3":
        for i, item in enumerate(tarefas, 1):
            print(f"{i}. {item}")
        
        try:
            num = int(input("Digite o número da tarefa para remover: "))
            indice_real = num - 1
            
            if 0 <= indice_real < len(tarefas):
                removido = tarefas.pop(indice_real)
                salvar_tarefas(tarefas)
                print(f"🗑️ Tarefa '{removido}' removida!")
            else:
                print("❌ Número inválido.")
        except ValueError:
            print("❌ Digite um número válido.")

    elif opcao == "4":
        print("Saindo... Até logo!")
        break
    
    else:
        print("❌ Opção inválida.")
# %%
2