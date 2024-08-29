import pygame
import random
import math

pygame.init()

score_1 = 0
score_2 = 0
test_font = pygame.font.Font('font/Pixeltype.ttf', 80)
text_surf = test_font.render('My game', False, (64, 64, 64))
text_rect = text_surf.get_rect(midbottom=(400, 80))

text1 = test_font.render(str(score_1), False, (64, 64, 64))
text1_rect = text1.get_rect(midbottom=(300, 150))

text2 = test_font.render(str(score_2), False, (64, 64, 64))
text2_rect = text1.get_rect(midbottom=(500, 150))

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Создание окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('My Game')

# Настройка таймера
clock = pygame.time.Clock()

# Мяч
shape = {
    "rect": pygame.Rect(100, 150, 50, 50),
    "color": random_color(),
    "speed": [5, 0],
    "radius": 20  # радиус круга
}

# Игроки (платформы)
player_speed = 5
player_1 = pygame.Rect(0, 0, 30, 130)
player_2 = pygame.Rect(770, 0, 30, 130)

def draw_dashed_line(screen, color, start_pos, end_pos, width, dash_length):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dl = dash_length
    dx = x2 - x1
    dy = y2 - y1
    steps = int(math.sqrt(dx**2 + dy**2) // dl)
    for i in range(steps):
        start = (x1 + dx * i / steps, y1 + dy * i / steps)
        end = (x1 + dx * (i + 0.5) / steps, y1 + dy * (i + 0.5) / steps)
        pygame.draw.line(screen, color, start, end, width)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if shape["rect"].collidepoint(mouse_pos):
                shape["color"] = random_color()

    keys = pygame.key.get_pressed()
    # Движение платформы игрока 1
    if keys[pygame.K_s] and player_1.bottom < 600:
        player_1.move_ip(0, player_speed)
    if keys[pygame.K_w] and player_1.top > 0:
        player_1.move_ip(0, -player_speed)

    # Движение платформы игрока 2
    if keys[pygame.K_DOWN] and player_2.bottom < 600:
        player_2.move_ip(0, player_speed)
    if keys[pygame.K_UP] and player_2.top > 0:
        player_2.move_ip(0, -player_speed)

    # Движение мяча
    shape["rect"].move_ip(shape["speed"])

    # Проверка на столкновение с границами экрана
    if shape["rect"].left < 0 or shape["rect"].right > 800:
        if shape["rect"].left <= 0:
            score_2 += 1  # Увеличиваем счет игрока 2
        else:
            score_1 += 1  # Увеличиваем счет игрока 1

        # Обновляем текст счета
        text1 = test_font.render(str(score_1), False, (64, 64, 64))
        text2 = test_font.render(str(score_2), False, (64, 64, 64))
        
        shape["speed"][0] = -shape["speed"][0]
        shape["color"] = random_color()

    if shape["rect"].top < 0 or shape["rect"].bottom > 600:
        shape["speed"][1] = -shape["speed"][1]
        shape["color"] = random_color()

    # Проверка на столкновение мяча с платформами
    if shape["rect"].colliderect(player_1) or shape["rect"].colliderect(player_2):
        # Рассчитываем угол отскока
        if shape["rect"].colliderect(player_1):
            offset = (shape["rect"].centery - player_1.centery) / player_1.height
        else:
            offset = (shape["rect"].centery - player_2.centery) / player_2.height

        angle = offset * math.pi / 4  # Максимальный угол отклонения 45 градусов
        shape["speed"][0] = -shape["speed"][0]
        shape["speed"][1] = int(5 * math.sin(angle))
        shape["color"] = random_color()

    # Очистка экрана
    screen.fill((135, 206, 235))

    # Отрисовка пунктирной линии
    draw_dashed_line(screen, 'black', (400, 0), (400, 600), 5, 20)
    pygame.draw.rect(screen, '#c0e8ec', text_rect)
    screen.blit(text_surf, text_rect)
    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    # Отрисовка объектов
    pygame.draw.circle(screen, shape["color"], shape["rect"].center, shape["radius"])
    pygame.draw.rect(screen, (64, 64, 64), player_1)
    pygame.draw.rect(screen, (64, 64, 64), player_2)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты кадров
    clock.tick(60)
