import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction,img_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
    def update(self):
        if self.direction = "right"
            self.rect.x += 10