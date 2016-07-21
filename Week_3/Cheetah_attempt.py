import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

YELLOW = (255, 255, 0)
BACKGROUND_COLOUR = (0, 0, 0)

#line(Surface, color, start_pos, end_pos, width=1)
screen.fill(BACKGROUND_COLOUR)
clock = pygame.time.Clock() 
done = False
while not done:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        #pygame.draw.arc(screen, YELLOW, Rect, 10, 90, 1)
        pygame.draw.line(screen, YELLOW, (150,100), (160, 100), 1)
        pygame.draw.line(screen, YELLOW, (160, 101), (163, 101), 1)
        pygame.draw.line(screen, YELLOW, (163, 100), (168, 100), 1)
        pygame.draw.line(screen, YELLOW, (169, 101), (172, 101), 1)



 
        pygame.display.flip()
 
        clock.tick(60)

pygame.quit
