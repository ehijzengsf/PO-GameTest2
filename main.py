import pygame

# Initialiseer Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock() # DIT IS BELANGRIJK

running = True
while running:
    # 1. Events afhandelen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Tekenen
    screen.fill((255, 255, 0)) # Jouw gele achtergrond
    
    # 3. Updaten
    pygame.display.flip()
    
    # 4. De "ademhaling" voor de browser:
    clock.tick(60)
