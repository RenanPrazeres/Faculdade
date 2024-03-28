import sys
def exibir_menu():
    print("MENU:")
    print("1.  Adicionar um Usuario")
    print("2. Exibir Lista Existente")
    print("3. Sair")

def adicionar_Usuario():
    # Logica para adicionar uma nova tarefa
    global pessoa 
    global preferencial
    global senha
    global contador_senha_c
    global contador_senha_p
    
    pessoa = []
    preferencial = []
    senha = []
    contador_senha_p = 1
    contador_senha_c = 1
        
    pessoa.append(input("Qual o seu nome:"))
    preferencial.append(input("Você é Preferencial? "))

    if preferencial == "sim":
        senha.append("P"+str(contador_senha_p))
        contador_senha_p+=1;
    else:
        senha.append("C"+str(contador_senha_c))
        contador_senha_c+=1;
    print("Novo Usuario Adicionado! ")

def exibir_Usuario():
    # Logica para adicionar as tarefas existentes

    i = 0

    for y in pessoa:
        print("ola,", pessoa[i], preferencial[i], "sua senha é: ", senha[i])
    i+= 1;
    #print("Tarefa existentes:")
    #print("- Tarefa 1")
    #print("- Tarefa 2")

def main():
    while True:
        exibir_menu()

        opcao = input("Escolha uma Opção: ")

        if opcao == "1":
            adicionar_Usuario()
        elif opcao == "2":
            exibir_Usuario()
        elif opcao == "3":
            sys.exit()
        else:
            print("Opção invalida. Tente Novamente.")
if __name__ == "__main__":
    main()