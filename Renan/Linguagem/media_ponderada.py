nota1= float(input("Digite a Primeira nota: "))
peso1 = float(input("Digite o peso da primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
peso2 = float(input("Digite o peso da segunda nota: "))
nota3 = float(input("Digite a Terceira nota: "))
peso3 = float(input("Digite o peso da terceira nota: "))

media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

if media_ponderada >= 6:
    situacao = "Aprovado"
else: 
    situacao = "Reprovado"

#(F) server para formatar uma string (Usado em Print)
print(f"A media ponderada é: {media_ponderada:.2f} e fim ")
print(f"A situação do aluno é: {situacao}")