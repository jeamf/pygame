import pygame
from pygame.locals import *
from sys import exit
import math

pygame.init()

SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

tank = pygame.image.load('tanque.jpg').convert()

x, y = 0, 0
tank_angle = 0

tank_speed = 0.5  # velocidade do tanque
tank_rotation_speed = 0.2  # velocidade de rotação

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[K_LEFT]:
        tank_angle += tank_rotation_speed
    if keys[K_RIGHT]:
        tank_angle -= tank_rotation_speed

    tank_angle %= 360

    tank_angle_radians = math.radians(tank_angle)
    tank_dx = tank_speed * math.cos(tank_angle_radians)
    tank_dy = tank_speed * math.sin(tank_angle_radians)

    if keys[K_DOWN]:
        x += tank_dx
        y -= tank_dy
    if keys[K_UP]:
        x -= tank_dx
        y += tank_dy

    mouse_x, mouse_y = pygame.mouse.get_pos()

    screen.fill((255, 255, 255))
    rotated_tank = pygame.transform.rotate(tank, tank_angle)
    tank_rect = rotated_tank.get_rect(center=(x, y))
    screen.blit(rotated_tank, tank_rect.topleft)

    pygame.display.update()
