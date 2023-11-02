import pygame
from pygame import mixer
import sys
import time


# player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("STARSHIP-01.png")
        self.rect = self.image.get_rect(center=(screen_width/2, screen_height/2))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("laser.png")
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):
        self.rect.y -= 20

# CPS counter
clicks = 0
start_time = time.time()
cps = 0

# general setup
print("What do you think your doing looking in here?")
pygame.init()
clock = pygame.time.Clock()
mixer.music.load("retro music.mp3")
screen_width, screen_height = 1000, 1200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.mouse.set_visible(False)

# define font and color
font = pygame.font.SysFont("arialblack", 40)
TEXT_COL = (255, 255, 255)

# functions

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# creating object
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

bullet_group = pygame.sprite.Group()

# main game loop
mixer.music.play()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mixer.music.stop()
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(player.create_bullet())
            clicks += 1

    # Calculate CPS
    elapsed_time = time.time() - start_time
    if elapsed_time > 0.5:  # Update CPS every second
        cps = clicks / elapsed_time
        start_time = time.time()
        clicks = 0

    # clear the screen
    screen.fill((12, 35, 67))

    # Display CPS on the screen
    font = pygame.font.Font(None, 36)
    cps_text = font.render(f"CPS: {cps:.2f}", True, (255, 255, 255))
    screen.blit(cps_text, (10, 10))

    # display instructions
    draw_text("Press SPACE to pause", font, TEXT_COL, 370, 1100)

    # Updating bullets and drawing
    bullet_group.update()
    player_group.draw(screen)
    bullet_group.draw(screen)
    player_group.update()

    # drawing
    bullet_group.update()
    player_group.draw(screen)
    bullet_group.draw(screen)
    player_group.update()
    pygame.display.flip()
    clock.tick(60)
