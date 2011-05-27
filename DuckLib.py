"""
Copyright 2011 Michael Bachmann

This program is distributed under the terms of the GNU
General Public License
"""

import pygame, random
pygame.init()

#Load in images
dogImg      =  [pygame.image.load("DogIdle.gif"),
                pygame.image.load("DogDuck.gif")]
duckImg     = [[pygame.image.load("duckUD1.gif"),
                pygame.image.load("duckUD2.gif"),
                pygame.image.load("DuckUD3.gif")],
               [pygame.image.load("DuckF1.gif"),
                pygame.image.load("DuckF2.gif"),
                pygame.image.load("DuckF3.gif")],
               [pygame.image.load("DuckShot.gif")],
               [pygame.image.load("DuckFall.gif"),
                pygame.transform.flip(pygame.image.load("DuckFall.gif"), True, False)]]
negaDuckImg = [[pygame.image.load("DarkwingSp.gif")],
               [pygame.image.load("DarkwingFlap.gif"),
                pygame.image.load("DarkwingFlap2.gif")]]

#Load in Sound
gunshot    = pygame.mixer.Sound("Gunshot.ogg")
quack      = pygame.mixer.Sound("Quack.ogg")

dSprites   = pygame.sprite.Group()
healthBars = pygame.sprite.Group()
flash      = pygame.sprite.Group()

score = 0

class NegaDuck(pygame.sprite.Sprite):

    def __init__(self, dogHand):
        pygame.sprite.Sprite.__init__(self)
        self.image         = negaDuckImg[0][0]
        self.image         = self.image.convert()
        self.image.set_colorkey((0,0,255))
        self.rect          = self.image.get_rect()
        self.rect.center   = (dogHand.rect.center)
        self.rect.centerx += 60
        self.changeDelay   = 0
        self.dog           = False
        self.enemy         = True


        #Death Animation Vars
        self.isDead    = False
        self.deadDelay = 10
        
        #Normal Animation Vars
        self.anim      = []
        self.animDelay = 15
        self.frame     = 0
        self.pause     = 0

        
        while 1:
            self.dx = random.randrange(-4,4)
            self.dy = random.randrange(-4,4)
            if not (self.dx,self.dy) == (0,0):
                break

        self.setAnim()
            
    def update(self):

        if not self.isDead:
            self.rect.centerx += self.dx
            self.rect.centery += self.dy
            self.changeDir()
            self.animate()

        else:
            self.anidead()

    def anidead(self):
        self.rect.centery += 3

        self.pause += 1
        if self.pause < 5:
            self.image = duckImg[2][0]
            self.image.set_colorkey((0,0,255))
        elif self.pause >= self.deadDelay:
            self.frame += 1
            self.pause = 5
            if self.frame >= len(self.anim):
                self.frame = 0
            self.image = self.anim[self.frame]

            self.image.set_colorkey((0,0,255))
        
    

    def animate(self):

        self.pause +=1
        if self.pause >= self.animDelay:
            self.frame +=1
            #print self.frame
            self.pause = 0
            if self.frame >= len(self.anim):
                self.frame = 0
            self.image = self.anim[self.frame]

            if self.dx < 0:
                self.image = pygame.transform.flip(self.image, True, False)

            self.image.set_colorkey((0,0,255))
            

    def changeDir(self):

        if self.rect.left < 0:
            while 1:
                self.dx        = random.randrange(0,4)
                self.dy        = random.randrange(-4,4)
                self.rect.left = 0
                if (self.dx,self.dy) != (0,0):
                    break
        if self.rect.right > 640:
            while 1:
                self.dx         = random.randrange(-4,0)
                self.dy         = random.randrange(-4,4)
                self.rect.right = 640
                if (self.dx,self.dy) != (0,0):
                    break
        if self.rect.top < 0:
            while 1:  
                self.dx       = random.randrange(-4,4)
                self.dy       = random.randrange(0,4)
                self.rect.top = 0
                if (self.dx,self.dy) != (0,0):
                    break
        if self.rect.bottom > 301:
            while 1:
                self.dx          = random.randrange(-4,4)
                self.dy          = random.randrange(-4,0)
                self.rect.bottom = 301
                if (self.dx,self.dy) != (0,0):
                    break

        self.setAnim()

    def setAnim(self):
      
        if self.isDead:
            self.anim = negaDuckImg[0]
        else:
            self.anim = negaDuckImg[1]



class Duck(pygame.sprite.Sprite):

    def __init__(self, dogHand):
        pygame.sprite.Sprite.__init__(self)
        self.image         = duckImg[2][0]
        self.image         = self.image.convert()
        self.image.set_colorkey((136,216,0))
        self.rect          = self.image.get_rect()
        self.rect.center   = (dogHand.rect.center)
        self.rect.centerx += 60
        self.changeDelay   = 0
        self.dog           = False
        self.enemy         = False


        #Death Animation Vars
        self.isDead    = False
        self.deadDelay = 10
        
        #Normal Animation Vars
        self.anim      = []
        self.animDelay = 15
        self.frame     = 0
        self.pause     = 0

        
        while True:
            self.dx = random.randrange(-4,4)
            self.dy = random.randrange(-4,4)
            if not (self.dx,self.dy) == (0,0):
                break

        self.setAnim()
            
    def update(self):


        if not self.isDead:
            self.rect.centerx += self.dx
            self.rect.centery += self.dy
            self.changeDir()
            self.animate()

        else:
            self.anidead()

    def anidead(self):
        self.rect.centery += 3

        self.pause += 1
        if self.pause < 5:
            self.image = duckImg[2][0]
            self.image.set_colorkey((136,216,0))
        elif self.pause >= self.deadDelay:
            self.frame += 1
            self.pause = 5
            if self.frame >= len(self.anim):
                self.frame = 0
            self.image = self.anim[self.frame]

            self.image.set_colorkey((136,216,0))
        
    

    def animate(self):

        self.pause +=1
        if self.pause >= self.animDelay:
            self.frame +=1
            #print self.frame
            self.pause = 0
            if self.frame >= len(self.anim):
                self.frame = 0
            self.image = self.anim[self.frame]

            if self.dx < 0:
                self.image = pygame.transform.flip(self.image, True, False)

            self.image.set_colorkey((136,216,0))
            

    def changeDir(self):

        if self.rect.left < 0:
            while 1:
                self.dx        = random.randrange(0,4)
                self.dy        = random.randrange(-4,4)
                self.rect.left = 0
                if (self.dx,self.dy) != (0,0):
                    break
        if self.rect.right > 640:
            while 1:
                self.dx         = random.randrange(-4,0)
                self.dy         = random.randrange(-4,4)
                self.rect.right = 640
                if (self.dx,self.dy) != (0,0):
                    break
        if self.rect.top < 0:
            while 1:
                self.dx       = random.randrange(-4,4)
                self.dy       = random.randrange(0,4)
                self.rect.top = 0
                if (self.dx,self.dy) != (0,0):
                    break
        if self.rect.bottom > 301:
            while 1:
                self.dx          = random.randrange(-4,4)
                self.dy          = random.randrange(-4,0)
                self.rect.bottom = 301
                if (self.dx,self.dy) != (0,0):
                    break

        #if score > 100:
    
            

        self.setAnim()

    def setAnim(self):
        
        if self.dy == 0:
            self.anim = duckImg[1]
        else:
            self.anim = duckImg[0]
        if self.isDead:
            self.anim = duckImg[3]

        
class Dog(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image        = dogImg[1]
        self.image        = self.image.convert()
        self.image.set_colorkey((0,0,255))
        self.rect         = self.image.get_rect()
        self.rect.center  = (random.randrange(45,595),440)
        self.spawn        = True
        self.release      = False
        self.retreat      = False
        self.dog          = True
        self.enemy        = False
        self.releaseSpeed = 2
        self.negaCounter  = 0
        global score

        
    def update(self):

        global score

        if score >= 100:
            self.releaseSpeed = 4
        elif score >=300:
            self.releaseSpeed = 5
        else:
            self.releaseSpeed = 2
            
        if self.spawn:
            self.rect.centery -= self.releaseSpeed
            if self.rect.top <= 200:
                self.spawn   = False
                self.release = True
                self.retreat = False
                self.image   = dogImg[0]
                self.image.set_colorkey((0,0,255))               

                
        elif self.release:

            self.negaCounter += 1
            if len(dSprites.sprites()) > 6 and self.negaCounter >= 6:
                dSprites.add(NegaDuck(self))
                self.negaCounter = 0
            else:
                dSprites.add(Duck(self))
                quack.play()
                
            self.spawn = False
            self.release = False
            self.retreat = True
        elif self.retreat:
            self.rect.centery += self.releaseSpeed
            if self.rect.top > 320:
                self.spawn   = True
                self.retreat = False
                self.release = False
                self.reset()

    def reset(self):

        self.rect.center = (random.randrange(45,595),440)
        self.spawn       = True
        self.image       = dogImg[1]
        self.image.set_colorkey((0,0,255))


class setPiece(pygame.sprite.Sprite):

    def __init__(self, image, topleft, layer):
        pygame.sprite.Sprite.__init__(self)
        self.image        = image
        self.image        = self.image.convert()
        self.image.set_colorkey( ( 0 , 0 , 255) )
        self.rect         = self.image.get_rect()
        self.rect.topleft = topleft
        self.layer        = layer

    def update(self):
        pass


class Crosshair(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image       = pygame.image.load("Crosshair.gif")
        self.image       = self.image.convert()
        self.rect        = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()

    def update(self):

        self.rect.center = pygame.mouse.get_pos()

        
class Flash(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image       = pygame.image.load("Gunshot.gif")
        self.image       = self.image.convert()
        self.rect        = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()
        self.pause       = 0

    def update(self):
        self.pause += 1
        if self.pause >= 5:
            flash.remove(self)


            
        
