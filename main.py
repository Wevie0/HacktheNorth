import pygame
import random

pygame.init()
pygame.font.init()

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

images = []
for i in range(8):
  
def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]	

level = 1
wrong = 0

fps = 60

run = True

chosen = ''
while run:  # Main Loop
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                chosen = 'a'
            if event.key == pygame.K_b:
                chosen = 'b'
            if event.key == pygame.K_c:
                chosen = 'c'
            if event.key == pygame.K_d:
                chosen = 'd'
            if event.key == pygame.K_e:
                chosen = 'e'
            if event.key == pygame.K_f:
                chosen = 'f'
            if event.key == pygame.K_g:
                chosen = 'g'
            if event.key == pygame.K_h:
                chosen = 'h'
            if event.key == pygame.K_i:
                chosen = 'i'
            if event.key == pygame.K_j:
                chosen = 'j'
            if event.key == pygame.K_k:
                chosen = 'k'
            if event.key == pygame.K_l:
                chosen = 'l'
            if event.key == pygame.K_m:
                chosen = 'm'
            if event.key == pygame.K_n:
                chosen = 'n'
            if event.key == pygame.K_o:
                chosen = 'o'
            if event.key == pygame.K_p:
                chosen = 'p'
            if event.key == pygame.K_q:
                chosen = 'q'
            if event.key == pygame.K_r:
                chosen = 'r'
            if event.key == pygame.K_s:
                chosen = 's'
            if event.key == pygame.K_t:
                chosen = 't'
            if event.key == pygame.K_u:
                chosen = 'u'
            if event.key == pygame.K_v:
                chosen = 'v'
            if event.key == pygame.K_w:
                chosen = 'w'
            if event.key == pygame.K_x:
                chosen = 'x'
            if event.key == pygame.K_y:
                chosen = 'y'
            if event.key == pygame.K_z:
                chosen = 'z'
    window.blit(background, (0, 0))
    for i in range(len(word)):
        pygame.draw.rect(window, (135, 223, 252), (i * 80 + 10, 680, 50, 10))
    if chosen in word and chosen != '':
        print(findOccurrences(word, chosen), word, chosen)
    elif chosen != '':
        wrong += 1
        print("The letter %s is not in the word." % chosen)
    chosen = ''
    pygame.display.update()
