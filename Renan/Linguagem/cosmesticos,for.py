produto = []
marca = []
preco = []
for x in range(5):
    produto.append(input("qual é o seu produto :"))
    marca.append(input("qual a marca  : "))
    preco.append(input("qual o valor : "))
p=0
for y in produto:
    print("O Produto:",produto[p],"da marca=>",marca[p],"com o preço:",preco[p])
    p+=1;
