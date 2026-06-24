class Pessoa:
  def __init__(self, nome: str, altura: float):
    self.nome = nome
    self.altura = altura
  def __str__(self):
    return f'Seu nome: {self.nome}, sua altura: {self.altura}'
  def __gt__(self, other):
    return self.altura > other.altura
  def __lt__(self, other):
    return self.altura < other.altura

qtd = int(input("quantas pessoas serão cadastradas?"))
cad = []
for i in range(qtd):
  print(f"\n--- Cadastro {i + 1} ---")
  nome = input("Digite o nome: ")
  altura = float(input("altura: "))
  pessoa = Pessoa(nome, altura)
  cad.append(pessoa)

print(f'Máximo: {max(cad)}')
print(f'Mínimo: {min(cad)}')

for pessoa in sorted(cad):
  print(f'---- LISTA DE CADASTRO ---- {pessoa}')
