import pygame
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
size=(700,500)  #width=700 height=500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ô Vuông Chạy")

done = False
clock = pygame.time.Clock()
rect_x=50

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill(WHITE)

    #pygame.draw.rect(screen,RED,[rect_x,50,50,50])  x,y,width,height
    pygame.draw.ellipse( screen, GREEN, [rect_x, 50, 50, 50] )
    rect_x +=1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()