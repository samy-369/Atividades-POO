class Carteira:
    def __init__(self, moeda, saldo):
        self.moedas = moeda
        self.saldo = saldo
    isin
   
  
        print(f'Adicionando {valor.nome}...', end='')
        if chave and chave < len(self):
            self.itens[chave] = valor
            print('pronto!')
        elif chave >= self.capacidade:
            print('Sua bolsa está cheia!')
        else:
            self.itens.append(valor)
            print('pronto!')

    # Método especial para verificar se um item está na bolsa
    # item in bag
    def __contains__(self, item):
        for potion in self.itens:
            if potion.nome == item: return True
        return False
