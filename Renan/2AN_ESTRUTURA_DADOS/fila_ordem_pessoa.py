filas = ['P0']

for x in range(4):   
    nome = input("Qual seu Nome? ")
    preferencial = input("Você é preferencial? Sim/Não " )

    if preferencial == "Sim":
        filas.insert(0, nome)

    else:
        filas.append(nome)

print(filas)