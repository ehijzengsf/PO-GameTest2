import asyncio
import pygame

async def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Teken hier je game
        screen.fill("purple")
        
        pygame.display.flip()
        await asyncio.sleep(0) # DIT IS VERPLICHT voor de browser

asyncio.run(main())
