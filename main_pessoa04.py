from pessoa04 import Pessoa 
lst = []
quantos = int(input("Quantas pessoas serão cadastradas?"))

for i range(quantidade):
  print(f"\n Pessoa {i + 1}")
  nome = input("Qual o nome?")
  altura = float(input("Qual a altura em metros?"))
  pessoa = Pessoa(nome, altura)
  lst.append(pessoa)

print("\n A pessoa mais alta é:")
print(max(lst))
print("\n A pessoa mais baixa é:")
print(min(lst))
print("\n Pessoas ordenadas por altura:")
for pessoa in sorted(lst):
  print(pessoa)
