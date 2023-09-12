import pygame
import random

pygame.init()

largura = 1280
altura = 720

janela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("Desenho de Retângulos e Círculos Aleatórios")

def gerar_cor_aleatoria():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    x = random.randint(0, largura)
    y = random.randint(0, altura)
    largura_retangulo = random.randint(20, 100)
    altura_retangulo = random.randint(20, 100)
    raio_circulo = random.randint(10, 50)
    cor_retangulo = gerar_cor_aleatoria()
    cor_circulo = gerar_cor_aleatoria()

    janela.fill((0, 0, 0))

    pygame.draw.rect(janela, cor_retangulo, (x, y, largura_retangulo, altura_retangulo))

    pygame.draw.circle(janela, cor_circulo, (x, y), raio_circulo)

    pygame.display.update()

pygame.quit()
