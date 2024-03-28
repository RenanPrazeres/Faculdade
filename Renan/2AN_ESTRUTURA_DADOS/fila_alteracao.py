#.append(Elemento):adicionar elemento ao final da lista;
#.insert(indice, elemento): isere elemento após a posição indice;
#.pop(indice): remove e retorna o elemento contido na posição indice.

fruta = ["pera", "uva"]
frutas = input("insira o nome da fruta: ")
fruta.append(frutas)

print(fruta)
print(fruta.pop(1))
print(fruta)
print(fruta.insert(1,'JACA'))
print(fruta)