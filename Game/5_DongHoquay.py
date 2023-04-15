import sys, pygame
from pygame.locals import *
import datetime

black = 0, 0, 0
white = 255, 255, 255

size = width, height = 390, 505
screen = pygame.display.set_mode( size )
pygame.display.set_caption( "VanTho15-PyGame" )
pygame.init()


class item:

    def __init__(self, imagename, colorkey, x, y):
        self.img = pygame.image.load( imagename ).convert()
        if colorkey == -1:
            ckey = self.img.get_at( (0, 0) )
            self.img.set_colorkey( ckey, RLEACCEL )
        self.x = x
        self.y = y

    def draw(self):
        screen.blit( self.img, (self.x, self.y) )

    def rotate(self, angle):
        self.newimg = pygame.transform.rotate( self.img, angle ).convert()
        self.newrect = self.newimg.get_rect( center=(self.x, self.y) )
        screen.blit( self.newimg, (self.newrect.left, self.newrect.top) )


bg = item( "D.png", 0, 0, 0 )
longhand = item( "p-01.png", -1, 195, 295 )
shorthand = item( "h-01.png", -1,  195, 295)
secondhand = item( "s-01.png", -1, 195, 295 )

while 1:

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit( 0 )

    bg.draw()

    now = datetime.datetime.now()
    hr = float( now.hour )
    mi = float( now.minute )
    sec = float( now.second )

    second = -360.0 / 60 * sec
    minute = -360.0 / 60 * mi

    hr1 = hr % 12
    hr2 = -360.0 / 12 * hr1
    temp = 360 / 12 / 60 * mi
    hour = hr2 - temp

    shorthand.rotate( hour )
    longhand.rotate( minute )
    secondhand.rotate( second )

    pygame.display.update()
    pygame.time.delay( 500 )

