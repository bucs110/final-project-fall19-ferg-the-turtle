import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
