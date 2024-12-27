import pygame
import random
pygame.init()

pygame.display.set_caption("Rocket In Space")
#(
WIDTH=700
HEIGHT=500

screen=pygame.display.set_mode([WIDTH,HEIGHT])#)

#Location of the player.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Lesson 8/Images/Rocket.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(80,100))#This will change the size of the image.
        self.rect=self.image.get_rect()
#keys
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)
        if pressed_keys[pygame.K_0]:
            self.rect.move_ip(random.randint(0,WIDTH),(0,HEIGHT))

    #keeping the player in the screen
        if self.rect.left <0:
           self.rect.left=0
        elif self.rect.right>WIDTH:
            self.rect.right=WIDTH
        if self.rect.top<0:
            self.rect.top=0
        elif self.rect.bottom>HEIGHT:
            self.rect.bottom=HEIGHT     
#end of class
class pizza(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Lesson 8/Images/pizza.jpg").convert_alpha()
        self.image=pygame.transform.scale(self.image,(80,100))#This will change the size of the image.
        self.rect=self.image.get_rect()


class noodle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Lesson 8/Images/noodle.jpg").convert_alpha()
        self.image=pygame.transform.scale(self.image,(80,100))#This will change the size of the image.
        self.rect=self.image.get_rect()

class burgerset(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Lesson 8/Images/burgerset.webp").convert_alpha()
        self.image=pygame.transform.scale(self.image,(80,100))#This will change the size of the image.
        self.rect=self.image.get_rect()

#group of sprites
sprites=pygame.sprite.Group()
burgergroup=pygame.sprite.Group()

def startgame():
    character=Player()
    sprites.add(character)
    burger=burgerset()
    burgergroup.add(burger)

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
        pressed_keys=pygame.key.get_pressed()
        character.update(pressed_keys)#calling update function
        #adding bg
        screen.blit(pygame.image.load("Lesson 8/Images/Space.png"),(0,0))

        #put the sprites on the screen
        sprites.draw(screen)
        pygame.display.update()
    
        
startgame()







