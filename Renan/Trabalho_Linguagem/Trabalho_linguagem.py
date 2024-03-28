'''#Resposta do Exercicio 01: (Comprimento Personalizado)
nome = input("Digite seu nome: ") #Variavel nome recebe o nome digitado pelo usuario atraves da entrada (input).
print(f"Bem vindo: {nome} !") #f minusculo na frente da string indica que sera uma string formatada/ print imprime o que esta na variavel.

#Resposta do Exercicio 02: (Validando Idade)
idade = int(input("Digite sua Idade: "))
if idade >= 18:
    print("Você é maior de Idade")
else:
    print("Você é menor de Idade")

#Resposta do Exercicio 03 (Calculadora Simples)
#Pegando Informações digitadas pelo Usuario
number1 = float(input(f"Digite o Seu Primeiro Numero: "))
number2 = float(input(f"Digite Seu Segundo Numero: "))
operacao = input(f"Digite a Operação Desejada: (SOMA/DIVISãO/MULTIPLICAÇÃO/SUBTRAÇÃO): ")

#Logica das operações matematicas 
if operacao == "SOMA" or operacao == "+": #

    print(f"O Resultado é: ", number1 + number2)

elif operacao == "SUBTRAÇÃO" or operacao == "-":
    print(f"O Resultado é: ", number1 - number2)

elif operacao == "MULTIPLICAÇÃO" or operacao == "*":
    print(f"O Resultado é: ", number1 * number2)

elif operacao == "DIVISÂO" or operacao == "/":
    print(f"O Resultado é: ", number1 / number2)

else:
    print("Opção invalida, Tente Novamente")'''

#Verificando Números Pares ou Impares

Numero = float(input("Digite Um Numero: "))
if Numero % 2 == 0 :
    print(f"O numero é PAR")
else:
    print(f"O numero é IMPAR")