import sys
import pygame
from src import hero
from src import bullet
from src import obstacle


class Controller:
    def __init__(self, width=640, height=480):
        self.background = None
        self.screen = pygame.display.set_mode((height, width))
        self.state = "GAME"
        self.width = width
        self.height = height
        self.hero = hero.Hero("Mort", (width / 3, height / 3), "image")
        self.obstacle = obstacle.Spikes("spikes",x,y,"image")
        self.white = (255, 255, 255)
        self.all_sprites = pygame.sprite.Group(self.hero)

    def mainLoop(self):
        while True:
            if self.state == "GAME":
                self.gameLoop()
            elif self.state == "EXIT":
                self.endLoop()
            elif self.state == "WIN"
                self.gameIntroScreen()
            elif self.state == "LOSE"
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
        self.drawText("Instructions of game", 20, self.white, self.width / 2, self.height / 2)
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
        pygame.key.set_repeat()
        while self.state == "GAME":
            self.background.fill()
            for event in pygame.events:
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if pygame.key == pygame.K_SPACE:
                        hero.Hero.jump("up")
            collides = pygame.sprite.spritecollide(self.hero,self.obstacle,True)
            if collides:
                for collision in collides:




    def endLoop(self):
        self.hero.kill()
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (0, 0, 0))
        self.screen.blit(message, (self.width / 2, self.height / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()