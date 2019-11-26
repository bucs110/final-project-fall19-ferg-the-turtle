import pygame



class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        pygame.sprite.Sprite.__init__(self)
        self.width, self.height = width, height
        self.pos_x, self.pos_y = pos_x, pos_y
        self.surface = pygame.surface.Surface((self.width, self.height))
        self.rect = self.surface.get_rect()
        self.surface.fill(color)
