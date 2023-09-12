import math
def calcular_superficie_retangulo(altura, largura):
    return altura * largura

def calcular_superficie_circulo(raio):
    return math.pi * (raio ** 2)

altura_retangulo = 5
largura_retangulo = 10
superficie_retangulo = calcular_superficie_retangulo(altura_retangulo, largura_retangulo)
print(f'A superfície do retângulo é {superficie_retangulo} unidades.')

raio_circulo = 3
superficie_circulo = calcular_superficie_circulo(raio_circulo)
print(f"A superfície do círculo é {superficie_circulo} unidades.")
