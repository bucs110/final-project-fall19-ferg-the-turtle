import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self, name, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = "right"
        self.speed = 3

    def jump(self, direction):
        if direction == "up":
            self.rect.y -= 10
