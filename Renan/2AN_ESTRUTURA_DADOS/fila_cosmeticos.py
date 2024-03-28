#.append(elemento): Adiciona elemento ao final da lista;
#.insert(indice, elemento): insere elemento após a posição indice;
#.pop(indice): remove e retorna o elemento contido na posição indice;


cosmetico = ['Perfume', 'sabone']
cosmeticos = input("Insira o nome do cosmetico: ")
cosmetico.append(cosmeticos)

print(cosmetico)
print(cosmetico.pop(0))
print(cosmetico)
print(cosmetico.insert(0,'lapis'))
print(cosmetico)