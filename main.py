import pygame
import random

pygame.init()

window = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Hangbot")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("tech-bg.png")

tech = ["technology", "boolean", "robot", "computer", "loop", "database"]
science = ["chemistry", "biology", "atom", "cell", "element", "physics"]
space = ["astronaut", "nebula", "stars", "moon", "satellite", "orbit", "galaxy"]

theme_list = [tech, science, space]

theme = random.choice(theme_list)

word = random.choice(theme)

fps = 60

run = True

while run:  # Main Loop
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.blit(background, (0, 0))
    pygame.display.update()    
