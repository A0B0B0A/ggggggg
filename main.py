from pygame import *


window = display.set_mode((1100,750))
FPS = 90
clock = time.Clock()

bg = image.load('background.png')
bg = transform.scale(bg,(1100,750))

p1 = image.load('sprite1.png')
p2 = image.load('sprite2.png')

class NPC(sprite.Sprite):
    def __init__(self, sprite_img, width, height, x, y):
        self.image = transform.scale(sprite_img, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

player1 = NPC(p1, 70, 70, 300, 300)
player2 = NPC(p2, 70, 70, 500, 300)

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(bg,(0,0))
    window.blit(player1.image, player1.rect)
    window.blit(player2.image, player2.rect)
    
    display.update()
    clock.tick(FPS)