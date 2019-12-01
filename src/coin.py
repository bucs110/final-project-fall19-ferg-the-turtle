import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = "SPIN"
        self.spin_sprite = ["assets/Sprites/goldCoin1.png", "assets/Sprites/goldCoin2.png",
        "assets/Sprites/goldCoin3.png", "assets/Sprites/goldCoin4.png", "assets/Sprites/goldCoin5.png",
        "assets/Sprites/goldCoin6.png", "assets/Sprites/goldCoin7.png", "assets/Sprites/goldCoin8.png",
        "assets/Sprites/goldCoin9.png"]
        self.spin_index = 0
    def spin(self):
        x = self.rect.x
        y = self.rect.y
        self.image = pygame.image.load(self.spin_sprite[self.spin_index]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # where im getting the error
        self.spin_index = (self.spin_index+1) % len(self.spin_sprite)
    def update(self):
        if self.state == "SPIN":
            self.spin()
