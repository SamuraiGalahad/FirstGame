import pygame
import random
import os

WIDTH = 400
HEIGHT = 400
FPS = 30

GREEN = (102, 222, 22)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, "p1_jump.png"))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        if self.rect.left > WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = WIDTH
        elif self.rect.top > HEIGHT:
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = HEIGHT


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

speed = 10

running = True
flLeft = flRight = False
flUp = flDown = False
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.rect.x -= speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.rect.x += speed
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.rect.y -= speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.rect.y += speed

    all_sprites.update()
    screen.fill((222, 75, 22))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()
