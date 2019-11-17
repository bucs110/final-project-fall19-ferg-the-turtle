import sys
import pygame
from hero import Hero


class Controller:
    def __init__(self, width=640, height=480):
        self.font_name = font_name
        self.background = None
        self.screen = pygame.display.set_mode((height, width))
        self.state = "GAME"
        self.width = width
        self.height = height
        self.mainCharacter = ("Mort", (width / 3, height / 3), "image")
        self.white = ((255, 255, 255))

    def mainLoop(self):
        while True:
            if self.state == "GAME":
                self.gameLoop()
            if self.state == "EXIT":
                self.endLoop()

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
                        Hero.jump("up")


    def endLoop(self):
        while True: