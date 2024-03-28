#.append(elemento): Adiciona elemento ao final da lista;
#.insert(indice, elemento): insere elemento após a posição indice;
#.pop(indice): remove e retorna o elemento contido na posição indice;


fruta = ['pera', 'uva']
frutas = input("Insira o nome da fruta: ")
fruta.append(frutas)

print(fruta)
print(fruta.pop(0))
print(fruta)
print(fruta.insert(0,'jaca'))
print(fruta)