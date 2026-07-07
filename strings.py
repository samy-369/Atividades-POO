# questão 01
nome = input("Digite seu primeiro nome:")
sobrenome = input("Digite seu sobrenome:")
print (f"Bem-vinda, {nome} {sobrenome}")

# questão 02
frase = input("Digite a frase:)
espacos = frase.count(" ")
print("\n Espaços em branco: {espacos}" 

# questão 03
nome = input("Digite seu nome: ")
escada = ""
for letra in nome:
    escada = escada + letra
    print(escada)

# questão 04
num = input("Número: ")
if len(num) == 9:
    if num[0] == "9":  
        print(f"Número Completo: {num[:5]}-{num[5:]}")
    else:
        print("Número Incorreto!")
elif len(num) == 8:
    print(f"Número Completo: 9{num[:4]}-{num[4:]}")
else:
    print("Número Incorreto!")

# questão 05
txt = input("Frase: ")
ind = []
qnt = 0
for i, letra in enumerate(txt):
    if letra in "AEIOUaeiou":
        ind.append(i)
        qnt += 1
print(f"Índices: {", ".join(ind)}")
print("Total:",qnt)
