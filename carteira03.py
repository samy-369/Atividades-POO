class Carteira:
    def __init__(self, moeda, saldo):
        self.moedas = moeda
        self.saldo = saldo
    def __add__ (self, other):
        if isinstance(other, CNY):
            return saldo (f"o saldo agora é " self.saldo + self.other)
        elif isinstance(other, USD):
            saldo = other * 0.14
            return saldo (f"o saldo agora é " self.saldo + self.other)
        elif isinstance(other, BRL):
            saldo = other * 0.85
            return saldo (f"o saldo agora é " self.saldo + self.other)
     def __sub__ (self, other):
        if isinstance(other, CNY):
            return saldo (f"o saldo agora é " self.saldo - self.other)
        elif isinstance(other, USD):
            saldo = other * 0.14
            return saldo (f"o saldo agora é " self.saldo - self.other)
        elif isinstance(other, BRL):
            saldo = other * 0.85
            return saldo (f"o saldo agora é " self.saldo - self.other)
