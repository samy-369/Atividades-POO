# questão 01
def contagem_caracteres(txt):
    dict = {}
    for l in txt:
        if l in dict:
            dict[l] += 1
        else:
            dict[l] = 1
    return dict

frase = "python programming"
result = contagem_caracteres(frase)
print(result)

#questão 03
def mesclar_dict(d1:dict,d2:dict):
    d3 = d1
    for elemento in d2:
        if elemento in d3:
            if d2[elemento] > d3[elemento]:
                d3[elemento] = d2[elemento]
        else:
            d3[elemento] = d2[elemento]
    return d3

dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 4, 'd': 5}
resultado = mesclar_dict(dicionario1, dicionario2)
print(resultado)

#questão 04
def filtrar_dict(dados:dict,chaves_filtradas:list):
    d = {}
    for elemento in chaves_filtradas:
        d[elemento] = dados[elemento]
    return d

dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves_filtradas = ['a', 'c', 'e']
resultado = filtrar_dict(dados, chaves_filtradas)
print(resultado)

#questão 05
def result_vota(votos:list):
    resultado = {}
    total = 0
    for dicionario in votos:
        for candidato in dicionario:
            if candidato in resultado:
                resultado[candidato] += dicionario[candidato]
                total += dicionario[candidato]
            else:
                resultado[candidato] = dicionario[candidato]
                total += dicionario[candidato]

    for candidato in resultado:
        resultado[candidato] = (candidato,resultado[candidato]/total*100)

    return resultado
votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]
resultado = result_vota(votos)
print(resultado)
