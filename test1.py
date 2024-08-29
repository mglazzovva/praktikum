import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Анимация фигур")

# Цвета
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Фигуры
shapes = [
    {"type": "rect", "rect": pygame.Rect(100, 150, 50, 50), "color": random_color(), "speed": [3, 0]},
    {"type": "rect", "rect": pygame.Rect(200, 300, 100, 50), "color": random_color(), "speed": [4, 0]},
    {"type": "circle", "center": [400, 100], "radius": 30, "color": random_color(), "speed": [2, 0]},
    {"type": "polygon", "points": [[500, 400], [550, 450], [500, 500], [450, 450]], "color": random_color(), "speed": [5, 0]},
]

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for shape in shapes:
                if shape["type"] == "rect" and shape["rect"].collidepoint(mouse_pos):
                    shape["color"] = random_color()
                elif shape["type"] == "circle":
                    distance = ((mouse_pos[0] - shape["center"][0]) ** 2 + (mouse_pos[1] - shape["center"][1]) ** 2) ** 0.5
                    if distance <= shape["radius"]:
                        shape["color"] = random_color()
                elif shape["type"] == "polygon":
                    if pygame.draw.polygon(screen, shape["color"], shape["points"], 0).collidepoint(mouse_pos):
                        shape["color"] = random_color()

    # Движение фигур
    for shape in shapes:
        if shape["type"] == "rect":
            shape["rect"].move_ip(shape["speed"])
            if shape["rect"].left < 0 or shape["rect"].right > width:
                shape["speed"][0] = -shape["speed"][0]
                shape["color"] = random_color()
        elif shape["type"] == "circle":
            shape["center"][0] += shape["speed"][0]
            if shape["center"][0] - shape["radius"] < 0 or shape["center"][0] + shape["radius"] > width:
                shape["speed"][0] = -shape["speed"][0]
                shape["color"] = random_color()
        elif shape["type"] == "polygon":
            for point in shape["points"]:
                point[0] += shape["speed"][0]
            if any(point[0] < 0 or point[0] > width for point in shape["points"]):
                shape["speed"][0] = -shape["speed"][0]
                shape["color"] = random_color()

    # Отрисовка
    screen.fill((255, 255, 255))  # Белый фон
    for shape in shapes:
        if shape["type"] == "rect":
            pygame.draw.rect(screen, shape["color"], shape["rect"])
        elif shape["type"] == "circle":
            pygame.draw.circle(screen, shape["color"], shape["center"], shape["radius"])
        elif shape["type"] == "polygon":
            pygame.draw.polygon(screen, shape["color"], shape["points"])

    pygame.display.flip()

    pygame.time.delay(30)

pygame.quit()
