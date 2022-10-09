import pygame
pygame.init()
running = True
#26, 119, 242
man = pygame.image.load("man.png")
bat = pygame.image.load("bat.png")
gun = pygame.image.load("gun.png")
pygame.display.set_caption("battle game")
screen = pygame.display.set_mode([1000, 1000])
screen.fill([255, 255, 255])
screen.blit(man, (1, 250))
screen.blit(man, (600, 250))
pygame.display.flip()
while running:
    screen = pygame.display.set_mode([1000, 1000])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_g]:
            print("test")
            screen.fill([255, 255, 255])
            screen.blit(bat, (100, 200))
            screen.blit(man, (1, 250))
            screen.blit(man, (600, 250))
            pygame.display.flip()
pygame.quit()