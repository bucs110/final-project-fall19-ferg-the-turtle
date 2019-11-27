import pygame
import itertools


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
        self.run_sprite = ["assets/Sprites/run 1.png", "assets/Sprites/run 2.png", "assets/Sprites/run 3.png",
                           "assets/Sprites/run 4.png", "assets/Sprites/run 5.png", "assets/Sprites/run 6.png"]
        self.jump_sprite = ["assets/Sprites/jump1.png", "assets/Sprites/jump2.png"]
        self.run_shoot_sprite = ["assets/Sprites/runshoot1.png", "assets/Sprites/runshoot2.png",
                                 "assets/Sprites/runshoot3.png", "assets/Sprites/runshoot4.png",
                                 "assets/Sprites/runshoot5.png", "assets/Sprites/runshoot6.png"]
    def run(self):
        for i in itertools.cycle(self.run_sprite):
            pygame.screen.flip(i)
            
    def jump(self, direction):
        if direction == "up":
            self.rect.y -= 10
