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
    def __init__(self, width=800, height=400):
        self.run = True
        self.screen = pygame.display.set_mode((width, height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.state = "BEGIN"
        self.height = height
        self.width = width
        self.jump = True
        self.run = True
        self.hero = hero.Hero("Johnny", self.width / 3, self.height / 3, "assets/Sprites/run 1.png","right","RUN")
        self.obstacles = pygame.sprite.Group() #add the obstacles into the group here
        self.hero = hero.Hero("Johnny", self.width / 3, self.height / 3, "assets/Sprites/run 1.png", "right", "RUN")
        self.wall = wall.Wall(self.rect.x, self.rect.y, 'assets/Sprites/stoneWall.png')
        self.obstacles = pygame.sprite.Group()
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.bullets = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group((self.hero,) + tuple(self.obstacles))
        self.score = pygame.time.Clock()

    def mainLoop(self):
        while self.run:
            if self.state == "BEGIN":
                self.gameIntroScreen()
            elif self.state == "GAME":
                self.gameLoop()
            elif self.state == "LOSE":
                self.gameOverScreen()

    def gameIntroScreen(self):
        self.hero.kill()
        background = pygame.image.load('assets/Sprites/space.png')
        background_size = self.screen.get_size()
        background_rect = background.get_rect()
        background_screen = pygame.display.set_mode(background_size)
        background_screen.blit(background, background_rect)
        my_font = pygame.font.SysFont(None, 40)
        title_font = pygame.font.SysFont(None, 50)
        name_of_game = title_font.render('Space Run', False, self.white)
        instructions = my_font.render('Hit space to jump, Hit "z" to shoot. Press space to play.', False, self.white)
        background_screen.blit(name_of_game, ((self.width / 3) + 50, self.height / 4))
        background_screen.blit(instructions, ((self.width / 3) - 220, self.height / 1.5))
        pygame.display.flip()
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.state = "GAME"
                        self.mainLoop()

    def gameOverScreen(self):
        self.hero.kill()
        background = pygame.image.load('assets/Sprites/Pygamespacebackground.jpg')
        # will get size of background image
        # if background_screen doesn't work, change to self.screen
        background_size = self.screen.get_size()
        background_img = self.screen.blit(background)
        background_rect = background.get_rect()
        background_screen = pygame.display.set_mode(background_size)
        background_screen.blit(background, background_rect)
        my_font = pygame.font.SysFont(None, 30)
        message = my_font.render('Game Over, Press space to play again.', False, (0, 0, 0))
        background_screen.blit(message, (self.width / 2, self.height / 2))
        pygame.display.flip()
        while self.state == "LOSE":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.state = 'GAME'
                        self.mainLoop()

    def update_platform(self):
        # needs work, still don't know how to do this
        plat = platform.Platform(self.width, 850, self.width / 3, self.height / 3, (0, 0, 255))
        self.screen.blit(self.screen, plat)
        pygame.display.flip()

    def gameLoop(self):
        pygame.time.delay(100)
        pygame.key.set_repeat(1, 50)
        while self.state == "GAME":
            while self.run:
                hero.Hero.run(self.hero)
                if (random.randrange(4) == 0):
                    self.obstacles.add(spikes.Spikes(self.rect.x, self.rect.y, 'assets/Sprites/spike.png'),
                                       wall.Wall(self.rect.x, self.rect.y, 'assets/Sprites/stoneWall.png'),
                                       coin.Coin(self.rect.x, self.rect.y))
                    self.update_platform()
                    pygame.display.flip()
            #self.update_platform()
            #self.sideScroller()

            self.background.fill(self.red)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:

                    if pygame.key == pygame.K_SPACE or pygame.K_UP:
                            #need to call update
                    if pygame.key == pygame.K_SPACE:
                            #need to call update 
                    elif pygame.key == pygame.K_z:
                        b = bullet.Bullet(self.hero.rect.centerx, self.hero.rect.centery, "right", "assets/Sprites/bullet.png")
                        self.bullets.add(b)
                        self.bullets.update()
                get_coin = pygame.sprite.spritecollide(self.hero, coin.Coin(self.rect.x, self.rect.y), True)
                bullet_collides = pygame.sprite.spritecollide(wall.Wall(self.rect.x, self.rect.y, 'assets/Sprites/stoneWall.png'), self.bullets, False)
                collides = pygame.sprite.spritecollide(self.hero, self.obstacles, True)
                bullet_collide_count = 0
                if collides:
                    self.state = "LOSE"
                while bullet_collide_count < 2:
                    if bullet_collides:
                        bullet_collide_count += 1
                else:
                    wall.Wall.kill()
                if get_coin:
                    coin.Coin.kill()
                    self.score += 10

                elif (random.randrange(4) == 0):
                    # in the loop, so will keep spawning objects, needs work though
                    self.obstacles.add(spikes.Spikes(self.rect.x, self.rect.y, 'assets/Sprites/spike.png'),
                                       wall.Wall(self.rect.x, self.rect.y, 'assets/Sprites/stoneWall.png'),
                                       coin.Coin(self.rect.x, self.rect.y))
                    self.update_platform()
                    pygame.display.flip()

                self.all_sprites.draw(self.screen)
                self.bullets.update()
                self.screen.blit(self.background, (0, 0))
                self.screen.blit(self.hero.image, (self.rect.x, self.rect.y))
                pygame.display.flip()

            self.all_sprites.draw(self.screen)
            pygame.display.flip()

    def sideScroller(self):
        background = pygame.image.load('assets/Sprites/Pygamespacebackground.jpg')
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
            pygame.display.flip()
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
