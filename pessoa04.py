class Pessoa:
    def __init__(self, nome, altura):
        self.nome = nome
        self.idade = altura
    def __str__(self):
        return f"Nome: {self.nome}, altura: {self.altura}"
    def __gt__(self, outro):
        return self.altura > outro.altura
    def __lt__(self, outro):
        return self.altura < outro.altura
