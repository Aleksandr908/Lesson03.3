import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-понг")

# Определение классов
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, dy):
        self.rect.y += dy
        # Ограничиваем движение ракетки в пределах экрана
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        self.dx = 5 * (-1 if random.choice([True, False]) else 1)  # Случайное направление
        self.dy = 5 * (-1 if random.choice([True, False]) else 1)

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Отскок от верхней и нижней границы
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy *= -1

        # Сброс мяча, если он выйдет за пределы ракеток
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.rect.x = WIDTH // 2 - BALL_SIZE // 2
            self.rect.y = HEIGHT // 2 - BALL_SIZE // 2
            self.dx *= -1  # Смена направления после сброса

# Создание объектов
player1 = Paddle(30, HEIGHT // 2 - PADDLE_HEIGHT // 2)
player2 = Paddle(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball()

# Основной игровой цикл
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление игроками
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.move(-10)
    if keys[pygame.K_s]:
        player1.move(10)
    if keys[pygame.K_UP]:
        player2.move(-10)
    if keys[pygame.K_DOWN]:
        player2.move(10)

    # Движение мяча
    ball.move()

    # Проверка на столкновение с ракетками
    if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
        ball.dx *= -1

    # Отрисовка объектов
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1.rect)
    pygame.draw.rect(screen, WHITE, player2.rect)
    pygame.draw.ellipse(screen, WHITE, ball.rect)

    pygame.display.flip()
    clock.tick(60)