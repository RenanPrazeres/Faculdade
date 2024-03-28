arrey = []
#Inicializa o valor Maximo com um valor muito pequeno
maximo = float('-inf') #menor numero em python('-inf')
#Loop para solicitar Numero ao usuario
while True:
    numero = int(input("Digite um numero inteiro "))
    arrey.append(numero)
    if numero <0:
        break #Sai do loop quando um numero negativo é inserido
    if numero > maximo:
        maximo = numero #Atualiza o valor maximo se necessario 

#Exibe o numero maximo encontrado
print(f"O numero maximo inserido foi: {maximo}")
#For arrey para amazernar os numero no arrey (lista)
for x in arrey:
    print(x)