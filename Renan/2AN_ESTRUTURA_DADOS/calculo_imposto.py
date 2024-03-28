salario_minimo = 1412
salario_func = float(input("qual o seu salario?"))

if salario_func > 5000:
    print("voce deve pagar imposto R$" , salario_func * 0,27)
elif salario_func > 2800:
     print("voce nao precisa pagar imposto", salario_func * 0,15)
else:
     print("Felizmente, voce nao ira pagar Imposto")