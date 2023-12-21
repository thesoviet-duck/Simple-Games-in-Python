# Imports
from pygame import mixer
import pygame
import sys
import time
import random
import button


# Game Variables
screen_width, screen_height = 1000, 1200
game_paused = True
menu_state = "main"

lives = 5
score = 0

clicks = 0
start_time = time.time()
cps = 0

enemy_spawn_timer = 0
enemy_spawn_delay = 0.5


# player class
class Player(pygame.sprite.Sprite):
    lives = 5

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Hero.png")
        self.rect = self.image.get_rect(center=(screen_width/2, screen_height/2))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

# Enemy class


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy_01.png") or pygame.image.load("enemy_02.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1000 - self.rect.width)
        self.rect.y = 0  # Initialize the enemy at the top of the screen
        self.speed = 8

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > screen_height:
            global lives
            lives -= 1
            self.rect.x = random.randint(0, 1000 - self.rect.width)
            self.rect.y = 0  # Reset the enemy at the top when it reaches the bottom


enemies = pygame.sprite.Group()


# Bullet Class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("laser.png")
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):
        self.rect.y -= 5


# general setup
pygame.display.set_caption("Space Invaders By ME!")
print("What do you think your doing looking in here?")
pygame.init()
clock = pygame.time.Clock()
mixer.music.load("retro music.mp3")
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.mouse.set_visible(False)
font = pygame.font.SysFont("arialblack", 40)
TEXT_COL = (255, 255, 255)

# functions


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def game_over():
    font.render("Game Over!", True, (0, 0, 0))


# Loading button pics
resume_button_pic = pygame.image.load("button_resume.png").convert_alpha()
quit_button_pic = pygame.image.load("button_quit.png").convert_alpha()
play_button_pic = pygame.image.load("button_play.png").convert_alpha()


# button Instances
resume_button = button.Button(400, 500, resume_button_pic, 1)
quit_button = button.Button(400, 600, quit_button_pic, 1)
play_button = button.Button(400, 500, play_button_pic, 1)
bg_image = pygame.image.load("background_image.jpg")

# creating object
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)
bullet_group = pygame.sprite.Group()


# main game loop
mixer.music.play()
while lives > 0:
    screen.blit(bg_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mixer.music.stop()
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(player.create_bullet())
            clicks += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True

    # Adding enemy
    if not game_paused:
        enemy_spawn_timer += 1 / 60

        # Spawn a new enemy if the timer exceeds the delay
        if enemy_spawn_timer > enemy_spawn_delay:
            enemy = Enemy()
            enemies.add(enemy)
            enemy_spawn_timer = 0  # Reset the timer

        # Update enemy positions
        enemies.update()

        # Check for collisions between bullets and enemies
        hits = pygame.sprite.groupcollide(enemies, bullet_group, True, True)

        if hits:
            score += 1

    # Calculate CPS
    elapsed_time = time.time() - start_time
    if elapsed_time > 0.5:  # Update CPS every point five second
        cps = clicks / elapsed_time
        start_time = time.time()
        clicks = 0

    # Display Lives
    font = pygame.font.Font(None, 36)
    cps_text = font.render(f"Lives: {lives:.0f}", True, (255, 255, 255))
    screen.blit(cps_text, (855, 50))

    # Display Score
    font = pygame.font.Font(None, 36)
    cps_text = font.render(f"Score: {score:.0f}", True, (255, 255, 255))
    screen.blit(cps_text, (850, 15))

    # Display CPS on the screen
    font = pygame.font.Font(None, 36)
    cps_text = font.render(f"CPS: {cps:.2f}", True, (255, 255, 255))
    screen.blit(cps_text, (50, 15))

    # check game is paused
    if game_paused:
        pygame.display.set_caption("Paused")
        # check menu state
        if menu_state == "main":
            # Display menu
            if play_button.draw(screen):
                game_paused = False
                menu_state = "paused"

            if quit_button.draw(screen):
                mixer.music.stop()
                pygame.quit()
                sys.exit()

        elif menu_state == "paused":
            # Display menu
            if resume_button.draw(screen):
                game_paused = False

            if quit_button.draw(screen):
                mixer.music.stop()
                pygame.quit()
                sys.exit()

    else:
        pygame.display.set_caption("Space Invaders By ME!")
        draw_text("Press SPACE to pause", font, TEXT_COL, 370, 1100)

    # Updating bullets and drawing
    bullet_group.update()
    player_group.draw(screen)
    bullet_group.draw(screen)
    player_group.update()

    # drawing
    enemies.draw(screen)
    bullet_group.update()
    player_group.draw(screen)
    bullet_group.draw(screen)
    player_group.update()
    pygame.display.flip()
    clock.tick(60)
