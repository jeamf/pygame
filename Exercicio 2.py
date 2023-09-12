import random
def gerar_cor_aleatoria():

    vermelho = random.randint(0, 255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)

    cor = (vermelho, verde, azul)

    return cor

cor_aleatoria = gerar_cor_aleatoria()
print(f"Cor aleatória: RGB{cor_aleatoria}")
