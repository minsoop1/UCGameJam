import pygame

SCREEN_WIDTH = 809
SCREEN_HEIGHT = 500
POS = (100, 100)

class Zombie(pygame.sprite.Sprite):

    def __init__(self, name, health, speed, sprite_image) -> None:
        super().__init__()
        self.name = name
        self.health = health
        self.speed = speed
        self.image = pygame.image.load(sprite_image)
        self.rect = self.image.get_rect()

    def update(self, inputs) -> None:
        if inputs[pygame.MOUSEBUTTONDOWN]:
            pass
            


    def take_damage(self, amount) -> None:
        self.health -= amount
        if self.health <= 0:
            self.kill()
            
    
 



