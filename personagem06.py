import random

class Personagem:
    def __init__(self, nome: str, vida: int):
        self.nome = nome
        self.vida = vida

    def tomar_dano(self, valor: int):
        self.vida = self.vida - valor


class Mago(Personagem):
    def __init__(self, nome: str, vida: int, mana: float):
        super().__init__(nome, vida)
        self.mana = mana
   
    def __str__(self):
        return f"O nome do mago é {self.nome} e ele tem {self.vida} de vida, e sua mana é {self.mana}."

    def __add__(self, valor: float):
        return self.mana + valor

    def __sub__(self, valor: float):
        if (self.mana - valor) > 0:
            return self.mana - valor
        elif (self.mana - valor) < 0:
            return "A mana não pode ser negativa"
        else:
            return 0

    def __mul__(self, fator: float):
        return self.mana * fator

    def __truediv__(self, valor: float):
        return self.mana / valor


class Barbaro(Personagem):
    def __init__(self, nome: str, vida: int, stamina: float):
        super().__init__(nome, vida)
        self.stamina = stamina
        self.furia = True

    def __str__(self):
        return f"O nome do bárbaro é  {self.nome} e ele tem {self.vida} de vida, e sua stamina: {self.stamina}"

    def __add__(self, valor: float):
        if not self.furia:
            return self.stamina + valor
        else:
            return (self.stamina + valor) * self.furia

    def __sub__(self, valor: float):
        self.stamina -= valor

        if self.stamina < 0:
            if not self.furia:
                self.furia = True
                self.stamina = 5.0
            else:
                self.stamina = 0.0

        return self.stamina

    def __mul__(self, fator: float):
        self.stamina *= fator

        if self.furia:
            self.vida += 5.0

        return self.stamina

    def __truediv__(self, valor: float):
        return self.stamina / valor


tipo = input("Qual o tipo de perssonagem (Mago ou Barbaro): ")

nome = input("Nome: ")
vida = int(input("Vida: "))

if tipo.lower() == "mago":
    mana = float(input("Mana: "))
    personagem = Mago(nome, vida, mana)

elif tipo.lower() == "barbaro":
    stamina = float(input("Stamina: "))
    personagem = Barbaro(nome, vida, stamina)

else:
    print("Tipo inválido!")
    exit()

while personagem.vida > 0:

    print("1 - Tomar poção simples")
    print("2 - Tomar poção especial")
    print("3 - Ataque básico")
    print("4 - Ataque especial")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        resultado = personagem + 5
        print("Resultado:", resultado)

    elif opcao == "2":
        resultado = personagem * 1.5
        print("Resultado:", resultado)

    elif opcao == "3":
        resultado = personagem - 2
        print("Resultado:", resultado)

    elif opcao == "4":
        resultado = personagem / 2
        print("Resultado:", resultado)

    elif opcao == "0":
        print("Jogo encerrado.")
        break

    else:
        print("Opção inválida!")
        continue

    dano = random.randint(1, 10)
    personagem.tomar_dano(dano)

    print(f"Dano recebido: {dano}")
    print(f"Vida atual: {personagem.vida}")
    print(personagem)

    if personagem.vida <= 0:
        print("Personagem derrotado!")
        break
