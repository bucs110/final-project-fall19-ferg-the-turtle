import sys
import pygame
import random
from src import hero
from src import bullet
from src import spikes
from src import wall
from src import coin


class Controller:
    def __init__(self, width=800, height=400):
        self.screen = pygame.display.set_mode((width, height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background_pic = 'assets/Sprites/space.png'
        self.state = "BEGIN"
        self.height = height
        self.width = width
        self.jump = True
        self.run = True
        self.hero = hero.Hero("Johnny", self.width / 3, self.height / 3, "assets/Sprites/run 1.png", "right", "RUN")
        self.obstacles = pygame.sprite.Group()
        self.wall = wall.Wall(self.width / 4, self.height - 240, 'assets/Sprites/stoneWall.png')
        # add the obstacles into the group here
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.coins = pygame.sprite.Group(coin.Coin(self.width / 5, self.height - 240, 'assets/Sprites/goldCoin1.png'))
        self.bullets = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group((self.hero,) + tuple(self.obstacles))
        self.score = pygame.time.Clock()

    def mainLoop(self):
        '''
        this method checks the state of the game and runs either the game, the game intro screen, or the game over screen.
        :param = None
        :returns = None
        '''
        while self.run:
            if self.state == "BEGIN":
                self.gameIntroScreen()
            elif self.state == "GAME":
                self.gameLoop()
            elif self.state == "LOSE":
                self.gameOverScreen()

    def gameIntroScreen(self):
        '''
        this method creates a game intro screen
        :param = None
        :returns = None
        '''
        self.hero.kill()
        background = pygame.image.load(self.background_pic)
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
        '''
        this method creates a game over screen.
        :param = None
        :returns = None
        '''
        self.hero.kill()
        background = pygame.image.load(self.background_pic)
        # will get size of background image
        # if background_screen doesn't work, change to self.screen
        background_size = self.screen.get_size()
        background_rect = background.get_rect()
        background_screen = pygame.display.set_mode(background_size)
        background_screen.blit(background, background_rect)
        my_font = pygame.font.SysFont(None, 30)
        message = my_font.render('Game Over, Press space to play again.', False, (255, 255, 255))
        background_screen.blit(message, ((self.width / 3) - 50, self.height / 3))
        pygame.display.flip()
        while self.state == "LOSE":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.state = 'GAME'
                        self.mainLoop()

    def gameLoop(self):
        '''
        this method runs the actual game. It also checks for all the game events
        :param = None
        :returns = None
        '''
        pygame.time.delay(100)
        background = pygame.image.load(self.background_pic)
        background_size = self.screen.get_size()
        background_rect = background.get_rect()
        background_screen = pygame.display.set_mode(background_size)
        background_screen.blit(background, background_rect)
        while self.state == "GAME":
            # self.side_Scroller()
            self.hero.run()
            if random.randrange(4) == 0:
                self.obstacles.add(spikes.Spikes(self.width / 3, self.height / 3, 'assets/Sprites/spike.png'),
                                   wall.Wall(self.width / 4, self.height / 4, 'assets/Sprites/stoneWall.png'),
                                   coin.Coin(self.width / 5, self.height / 5, 'assets/Sprites/goldCoin1.png'))
                self.all_sprites.draw(self.screen)
                pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or pygame.K_UP:
                        self.hero.jump()
                    elif event.key == pygame.K_z:
                        b = bullet.Bullet(self.hero.rect.centerx, self.hero.rect.centery, "right",
                                          "assets/Sprites/bullet.png")
                        self.bullets.add(b)
                        self.bullets.update()

            get_coin = pygame.sprite.spritecollide(self.hero, self.coins, True)
            bullet_collides = pygame.sprite.spritecollide(self.wall, self.bullets, True)
            collides = pygame.sprite.spritecollide(self.hero, self.obstacles, True)
            if collides:
                self.state = "LOSE"
            elif bullet_collides:
                self.wall.kill()
            elif get_coin:
                self.coins.kill()
                self.score += 10

            self.bullets.update()
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.hero.image, (self.hero.rect.x, self.hero.rect.y))
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

    def side_Scroller(self):
        '''
        this method continuously scrolls the screen as the game runs.
        :param = None
        :returns = None
        '''
        background = pygame.image.load('assets/Sprites/space.png')
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
                    sys.exit()
            y1 += 5
            y += 5
            screen.blit(background, (x, y))
            screen.blit(background, (x1, y1))
            if y > h:
                y = -h
            elif y1 > h:
                y1 = h
            pygame.display.flip()
