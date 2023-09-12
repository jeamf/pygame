import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1280, 720), 0, 32)

def create_scales(height):
    red_scale_surface = pygame.surface.Surface((640, height))
    green_scale_surface = pygame.surface.Surface((640, height))
    blue_scale_surface = pygame.surface.Surface((640, height))
    for x in range(640):
        c = int((x / 639.) * 255.)
        red = (c, 0, 0)
        green = (0, c, 0)
        blue = (0, 0, c)
        line_rect = Rect(x, 0, 1, height)
        pygame.draw.rect(red_scale_surface, red, line_rect)
        pygame.draw.rect(green_scale_surface, green, line_rect)
        pygame.draw.rect(blue_scale_surface, blue, line_rect)
    return red_scale_surface, green_scale_surface, blue_scale_surface

red_scale, green_scale, blue_scale = create_scales(80)

color = [127, 127, 127]

while True:
    import pygame
    from pygame.locals import *
    from sys import exit

    pygame.init()

    screen = pygame.display.set_mode((640, 480), 0, 32)

    def leap_color(color1, color2, alpha):
        r = int(color1[0] + (color2[0] - color1[0]) * alpha)
        g = int(color1[1] + (color2[1] - color1[1]) * alpha)
        b = int(color1[2] + (color2[2] - color1[2]) * alpha)
        return (r, g, b)


    colors = [
        (255, 0, 0),  # Red
        (255, 165, 0),  # Orange
        (255, 255, 0),  # Yellow
        (0, 255, 0),  # Green
        (0, 0, 255),  # Blue
        (128, 0, 128)  # Purple
    ]

    rectangles = []

    for i, color in enumerate(colors):
        rect_height = 480 // len(colors)
        rect = pygame.Rect(0, i * rect_height, 640, rect_height)
        rectangles.append((rect, color, 0.0))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for i, (rect, color, alpha) in enumerate(rectangles):
            if rect.collidepoint(mouse_x, mouse_y):
                alpha += 0.01
                if alpha >= 1.0:
                    alpha = 0.0

                color1 = colors[i]
                color2 = colors[(i + 1) % len(colors)]
                interpolated_color = leap_color(color1, color2, alpha)

                rectangles[i] = (rect, interpolated_color, alpha)

        screen.fill((0, 0, 0))

        for rect, color, _ in rectangles:
            pygame.draw.rect(screen, color, rect)

        pygame.display.update()
        clock.tick(60)
