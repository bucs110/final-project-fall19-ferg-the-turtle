import pygame



class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        self.width, self.height = width, height
        self.pos_x, self.pos_y = pos_x, pos_y
        pygame.sprite.Sprite.__init__(self)
        self.surface = pygame.surface.Surface((self.width, self.height))
        self.rect = self.surface.get_rect(self.pos_x, self.pos_y)
        self.surface.fill(color)






