import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode( size )
pygame.display.set_caption( "Ô Tô" )

done = False

clock = pygame.time.Clock()

carImg = pygame.image.load( 'xe2.png' )
angle = 0

def placeCar(x, y):
    screen.blit( carImg, (x, y) )

def rotateCar(x, y, angle):
    rotatedCar = pygame.transform.rotate( carImg, angle )
    rot_rect = rotatedCar.get_rect( center=(x, y) )
    screen.blit( rotatedCar, (rot_rect.left, rot_rect.top) )


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                angle -= 10
            elif event.key == pygame.K_LEFT:
                angle += 10

    screen.fill( WHITE )
    # placeCar(100, 200)
    if angle > 360:
        angle = 0
    if angle < 0:
        angle = 360
    rotateCar( 200, 200, angle )


    pygame.display.flip()
    clock.tick( 60 )
pygame.quit()

