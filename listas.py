# questão 01
lista = [int(x) for x in input("Números Inteiros separados por espaço: ").split()]
print(lista)
print(lista[2:])
print(lista[-2:])
print(lista[::-1])
print(lista[::2])
print(lista[1::2])

#questão 02
URLs = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
print([dominio[4:-4] for dominio in URLs])

#questão 03
import random
list = [random.randint(-100,100) for x in range(10)]
print(sorted(list))
print(list)
print(list.index(max(list)))
print(list.index(min(list)))
soma = 0
for n in lista:
    soma += n
print(soma)
print(soma/10)

#questão 04
list_1 = [int(x) for x in input("Lista1 separada por espaço: ").split()]
list_2 = [int(x) for x in input("Lista2 separada por espaço: ").split()]
list_3 = []
for i in range(max(len(list_1),len(list_2))-1):
    try:
        list_3.append(list_1[i])
    except:
        pass
    try:
        list_3.append(list_2[i])
    except:
        pass
print(list_3)

#questão 05
import random
list_1 = [random.randint(0,50) for x in range(10)]
list_2 = [random.randint(0,50) for x in range(10)]
list_inter = []
for elemento in list_1:
    if elemento in list_2 and elemento not in list_inter:
        list_inter.append(elemento)
print(list_1)
print(list_2)
print(list_inter)

#questão 06
import random
lista = [random.randint(0,100) for x in range(20)]
tam = int(input("Tamanho para divisão: "))
lista_ofc =[]
for i in range(0,len(lista),tam):
    lista_ofc.append(lista[i:i+tam])
print(lista_ofc)

#questão 07
matriz = []
for i in range(n :=int(input("Digte n:"))):
    matriz.append([i for _ in range(n)])
print(matriz)
