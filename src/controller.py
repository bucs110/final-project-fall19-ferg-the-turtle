import sys
import pygame
import random
from src import hero
from src import bullet
from src import spikes
from src import wall
from src import platform
from src import coin


class Controller:
    def __init__(self, width=640, height=480):
        self.running = True
        self.background = None
        self.screen = pygame.display.set_mode((height, width))
        self.state = "GAME"
        self.width = width
        self.height = height
        self.run_sprite = ["assets/Sprites/run 1.png", "assets/Sprites/run 2.png", "assets/Sprites/run 3.png",
                           "assets/Sprites/run 4.png", "assets/Sprites/run 5.png", "assets/Sprites/run 6.png"]
        self.jump_sprite = ["assets/Sprites/jump1.png", "assets/Sprites/jump2.png"]
        self.run_shoot_sprite = ["assets/Sprites/runshoot1.png", "assets/Sprites/runshoot2.png",
                                 "assets/Sprites/runshoot3.png", "assets/Sprites/runshoot4.png",
                                 "assets/Sprites/runshoot5.png", "assets/Sprites/runshoot6.png"]

        self.hero = (hero.Hero("Johnny", self.width / 3, self.height / 3, "assets/Sprites/run 1.png"))
        self.obstacles = pygame.sprite.Group()
        self.bullet = None
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.all_sprites = pygame.sprite.Group((self.hero,) + tuple(self.obstacles))
        self.platforms = pygame.sprite.Group()
        self.score = 0
        self.coins = pygame.sprite.Group()

    def mainLoop(self):
        while self.running:
            if self.state == "GAME":
                self.gameLoop()
            elif self.state == "BEGIN":
                self.gameIntroScreen()
            elif self.state == "LOSE":
                self.gameOverScreen()

    def gameIntroScreen(self):
        self.hero.kill()
        background = pygame.image.load('assets/Sprites/Pygamespacebackground.jpg')
        # need a background image
        # will get size of background image
        background_size = background.get_size()
        background_rect = background.get_rect()
        background_screen = pygame.display.set_mode(background_size)
        background_screen.blit(background, background_rect)
        my_font = pygame.font.SysFont(None, 30)
        name_of_game = my_font.render('Space Run', False, self.white)
        instructions = my_font.render('Hit space to jump, Hit "z" to shoot. Press any key to play.', False, self.white)
        background_screen.blit(name_of_game, (self.width / 2, self.height / 2))
        background_screen.blit(instructions, (self.width / 2, self.height / 4))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.state = "GAME"

    def gameOverScreen(self):
        self.hero.kill()
        background = pygame.image.load('assets/Sprites/Pygamespacebackground.jpg')
        # will get size of background image
        # if background_screen doesn't work, change to self.screen
        background_size = background.get_size()
        background_rect = background.get_rect()
        background_screen = pygame.display.set_mode(background_size)
        background_screen.blit(background, background_rect)
        my_font = pygame.font.SysFont(None, 30)
        message = my_font.render('Game Over, Press any key to play again.', False, (0, 0, 0))
        background_screen.blit(message, (self.width / 2, self.height / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.state = "GAME"

    def update_platform(self):
        # needs work, still don't know how to do this
        platform1 = platform.Platform(self.width, 50, self.width / 3, self.height / 3, (0, 0, 255))
        self.screen.blit(platform1)
        pygame.display.flip()

    def gameLoop(self):
        self.gameIntroScreen()
        pygame.key.set_repeat(1, 50)
        while self.state == "GAME":
            self.update_platform()
            self.sideScroller()
            self.background.fill(self.red)
            for event in pygame.events:
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if pygame.key == pygame.K_SPACE:
                        hero.Hero.jump('up')
                    elif pygame.key == pygame.K_z:
                        if self.bullet is not None:
                            self.bullet.kill()
                        self.bullet = bullet.Bullet(self.hero.rect.centerx, self.hero.rect.centery, "right",
                                                    "assets/Sprites/bullet.png")
                        self.all_sprites.add(self.bullet)
            if (random.randrange(4) == 0):
                # in the loop, so will keep spawning objects, needs work though
                self.obstacles.add(spikes.Spikes('how do we get this on the platform', ), wall.Wall('same here'), )
                self.screen.blit(self.obstacles)
                pygame.display.flip()

            get_coin = pygame.sprite.spritecollide(self.hero, coin.Coin(), True)
            bullet_collides = pygame.sprite.spritecollide(self.bullet, wall.Wall, False)
            collides = pygame.sprite.spritecollide(self.hero, self.obstacles, True)
            bullet_collide_count = 0
            if collides:
                self.state = "LOSE"
            elif bullet_collides:
                bullet_collide_count += 1
                if bullet_collide_count > 20:
                    wall.Wall.kill()
            elif (self.bullet is not None):
                self.bullet.update()
            elif get_coin:
                coin.Coin.kill()
                self.score += 10

            self.all_sprites.draw(self.screen)
            pygame.display.flip()

    def sideScroller(self):
        background = pygame.image.load('background image')
        # will get size of background image
        # may need to go inside gameLoop()
        background_size = background.get_size()
        background_rect = background.get_rect()
        screen = pygame.display.set_mode(background_size)
        w, h = background_size
        x = 0
        y = 0

        x1 = 0
        y1 = -h
        run = True

        while run:
            screen.blit(background, background_rect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            y1 += 5
            y += 5
            screen.blit(background, (x, y))
            screen.blit(background, (x1, y1))
            if y > h:
                y = -h
            elif y1 > h:
                y1 = h
            pygame.display.flip()
            pygame.time.Clock.tick(10)
