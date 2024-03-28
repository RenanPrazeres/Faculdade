N1 = float(input("Qual Sua Nota1: "))
N2 = float(input("Qual Sua Nota2: "))

media = (N1 + N2)/2

if media > 6:
    print("Aluno Aprovados, sua media ficou em:", media)
elif media >= 5:
    print("Aluno Recuperação N3 , sua media ficou em:", media)
else:
    print("Aluno Reprovado, sua media ficou em:", media)