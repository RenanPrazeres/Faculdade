pessoa = []
parentesco = []
senha  = []
contador = 1
preferencial = 2


for x in range(3):
    pessoa.append(input("qual é o seu nome ? :"))
    parentesco.append(input("qual é o seu parentesco? :"))
    senha.append(contador)
    senha.append(preferencial)
    preferencial=0
    contador +=1
i=0


for y in pessoa:
    print("Olá Senhor (a)",pessoa[i],parentesco[i],"Sua Senha é ",senha[i])
    i+=1;