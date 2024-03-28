pessoa = []
preferencial = []
senha = []
contador_senha_p = 1
contador_senha_c = 1

for x in range(4):
    pessoa.append(input("Qual o seu nome:"))
    preferencial.append(input("Você é Preferencial? "))

    if preferencial[x] == "sim":
        senha.append("P"+str(contador_senha_p))
        contador_senha_p+=1;
    else:
        senha.append("C"+str(contador_senha_c))
        contador_senha_c+=1;

i = 0

for y in pessoa:
    print("ola,", pessoa[i], preferencial[i], "sua senha é: ", senha[i])
    i+= 1;

