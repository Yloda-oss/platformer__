import pygame


pygame.init()


WIDTH = 36 * 32
HEIGHT = 10 * 32
SIZE = ([WIDTH, HEIGHT])
TITLE = "_____________________________________"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


clock = pygame.time.Clock()
refresh_rate = 60


WHITE = (255, 255, 255)
GRAY = (175, 175, 175)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            

    screen.fill(WHITE)

    for x in range(0, WIDTH, 32):
        pygame.draw.line(screen, GRAY, [x, 0], [x, HEIGHT], 1)

    for y in range(0, HEIGHT, 32):
        pygame.draw.line(screen, GRAY, [0, y], [WIDTH, y], 1)


    pygame.display.flip()


    clock.tick(refresh_rate)


pygame.quit()
