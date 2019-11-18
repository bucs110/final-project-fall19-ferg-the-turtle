import sys
import pygame
from src import hero
from src import bullet
from src import spikes
from src import wall


class Controller:
    def __init__(self, width=640, height=480):
        self.running = True
        self.background = None
        self.screen = pygame.display.set_mode((height, width))
        self.state = "GAME"
        self.width = width
        self.height = height
        self.hero = hero.Hero("Mort", (width / 3, height / 3), "image")
        #need to find out how to randomly spawn objects
        self.obstacles = pygame.sprite.Group((spikes.Spikes,), (wall.Wall,))
        self.bullets = pygame.sprite.Group()
        self.white = (255, 255, 255)
        self.red = (255,0,0)
        self.all_sprites = pygame.sprite.Group((self.hero,) + (self.obstacles,) + (self.bullets,))

    def mainLoop(self):
        while self.running:
            if self.state == "GAME":
                self.gameLoop()
            elif self.state == "EXIT":
                self.endLoop()
            elif self.state == "BEGIN":
                self.gameIntroScreen()
            elif self.state == "LOSE":
                self.gameOverScreen()

    def drawText(self, text, font_name, font_size, x, y):
        font = pygame.font.Font(font_name, font_size)
        text_surface = font.render(text, True, font_name)
        text_rect = text_surface.get_rect()
        text_rect.mid_top = (x, y)
        self.screen.blit(text_surface, text_rect)

    def gameIntroScreen(self):
        self.screen.fill((255, 0, 0))
        self.drawText("TITLE", 48, self.white, self.width / 2, self.height / 4)
        self.drawText("Space to jump up, right arrow to shoot", 20, self.white, self.width / 2, self.height / 2)
        self.drawText("Press any key to play", 20, self.white, self.width / 2, self.height * 3 / 4)
        pygame.display.flip()
        self.pressKeyToStart()

    def gameOverScreen(self):
        self.screen.fill((255, 0, 0))
        self.drawText("GAME OVER", 48, self.white, self.width / 2, self.height / 4)
        self.drawText("Score: maybe?", 20, self.white, self.width / 2, self.height / 2)
        self.drawText("Press any key to play again", 20, self.white, self.width / 2, self.height * 3 / 4)
        pygame.display.flip()
        self.pressKeyToStart()

    def pressKeyToStart(self):
        wait = True
        while wait:
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.endLoop()
                elif event.type == pygame.KEYUP:
                    wait = False

    def gameLoop(self):
        self.state = "BEGIN"
        pygame.key.set_repeat()
        if self.pressKeyToStart():
            self.state = "GAME"
        while self.state == "GAME":
            self.background.fill(self.red)
            for event in pygame.events:
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if pygame.key == pygame.K_SPACE:
                        hero.Hero.jump('up')
            collides = pygame.sprite.spritecollide(self.hero, self.obstacles, True)
            bullet_collides = pygame.sprite.spritecollide(self.bullets, wall.Wall, True)
            b = bullet.Bullet(60, 48, "right", "image")
            self.bullets.add(b)
            if collides:
                self.state = "LOSE"
            elif bullet_collides:
                #if the bullet collides with the wall
                wall.Wall.kill()



    def sideScroller(self):
        background = pygame.image.load('background image')
        #will get size of background image
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
            screen.blit(background,background_rect)
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
            pygame.display.update()
            pygame.time.Clock.tick(10)


    def endLoop(self):
        #copied from lab, needs work
        self.hero.kill()
        my_font = pygame.font.SysFont(None, 30)
        message = my_font.render('Game Over', False, (0, 0, 0))
        self.screen.blit(message, (self.width / 2, self.height / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()