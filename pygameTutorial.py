##Kimberly Winter 		10/19/16
##Pygame tutorial- Bouncing ball :)

import sys, pygame
pygame.init()

size = width, height = 2048, 1028
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

#ball = pygame.image.load("football.png")
#ballrect = ball.get_rect()

class ball(object):
    def __init__(self):
        self.ball=pygame.image.load("football.png")
        self.ballrect=self.ball.get_rect()

ball1=ball()
while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
            	sys.exit()
#        ballrect = ballrect.move(speed)
 #       if ballrect.left < 0 or ballrect.right > width:
  #          speed[0] = -speed[0]
   #     if ballrect.top < 0 or ballrect.bottom > height:
    #        speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball1.ball, ball1.ballrect)
        pygame.display.flip()