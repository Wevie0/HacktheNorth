import pygame
import pygame.freetype
import random

pygame.init()

window = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Hangbot")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("tech-bg.png")
gameFont = pygame.freetype.Font("Consolas.ttf", 48)

tech = ["technology", "boolean", "robot", "computer", "loop", "database", "javascript", "python"]
science = ["chemistry", "biology", "atom", "cell", "element", "physics"]
space = ["astronaut", "nebula", "stars", "moon", "satellite", "orbit", "galaxy"]

theme_list = [tech, science, space]

theme = random.choice(theme_list)
word = random.choice(theme)
word = "chemistry"

level = 1
wrong = 0
run = True


def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


correct = []
incorrect = []
keys_chosen = []
while run:  # Main Loop
    chosen = ''
    window.fill((255, 255, 255))
    window.blit(background, (0, 0))
    BLUE = (133, 138, 227)
    PURPLE = (97, 61, 193)
    pygame.draw.rect(window, PURPLE, (390, 90, 470, 170))
    pygame.draw.rect(window, BLUE, (400, 100, 450, 150))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and 'a' not in keys_chosen:
                chosen = 'a'
                keys_chosen.append('a')
            if event.key == pygame.K_b and 'b' not in keys_chosen:
                chosen = 'b'
                keys_chosen.append('b')
            if event.key == pygame.K_c and 'c' not in keys_chosen:
                chosen = 'c'
                keys_chosen.append('c')
            if event.key == pygame.K_d and 'd' not in keys_chosen:
                chosen = 'd'
                keys_chosen.append('d')
            if event.key == pygame.K_e and 'e' not in keys_chosen:
                chosen = 'e'
                keys_chosen.append('e')
            if event.key == pygame.K_f and 'f' not in keys_chosen:
                chosen = 'f'
                keys_chosen.append('f')
            if event.key == pygame.K_g and 'g' not in keys_chosen:
                chosen = 'g'
                keys_chosen.append('g')
            if event.key == pygame.K_h and 'h' not in keys_chosen:
                chosen = 'h'
                keys_chosen.append('h')
            if event.key == pygame.K_i and 'i' not in keys_chosen:
                chosen = 'i'
                keys_chosen.append('i')
            if event.key == pygame.K_j and 'j' not in keys_chosen:
                chosen = 'j'
                keys_chosen.append('j')
            if event.key == pygame.K_k and 'k' not in keys_chosen:
                chosen = 'k'
                keys_chosen.append('k')
            if event.key == pygame.K_l and 'l' not in keys_chosen:
                chosen = 'l'
                keys_chosen.append('l')
            if event.key == pygame.K_m and 'm' not in keys_chosen:
                chosen = 'm'
                keys_chosen.append('m')
            if event.key == pygame.K_n and 'n' not in keys_chosen:
                chosen = 'n'
                keys_chosen.append('n')
            if event.key == pygame.K_o and 'o' not in keys_chosen:
                chosen = 'o'
                keys_chosen.append('o')
            if event.key == pygame.K_p and 'p' not in keys_chosen:
                chosen = 'p'
                keys_chosen.append('p')
            if event.key == pygame.K_q and 'q' not in keys_chosen:
                chosen = 'q'
                keys_chosen.append('q')
            if event.key == pygame.K_r and 'r' not in keys_chosen:
                chosen = 'r'
                keys_chosen.append('r')
            if event.key == pygame.K_s and 's' not in keys_chosen:
                chosen = 's'
                keys_chosen.append('s')
            if event.key == pygame.K_t and 't' not in keys_chosen:
                chosen = 't'
                keys_chosen.append('t')
            if event.key == pygame.K_u and 'u' not in keys_chosen:
                chosen = 'u'
                keys_chosen.append('u')
            if event.key == pygame.K_v and 'v' not in keys_chosen:
                chosen = 'v'
                keys_chosen.append('v')
            if event.key == pygame.K_w and 'w' not in keys_chosen:
                chosen = 'w'
                keys_chosen.append('w')
            if event.key == pygame.K_x and 'x' not in keys_chosen:
                chosen = 'x'
                keys_chosen.append('x')
            if event.key == pygame.K_y and 'y' not in keys_chosen:
                chosen = 'y'
                keys_chosen.append('y')
            if event.key == pygame.K_z and 'z' not in keys_chosen:
                chosen = 'z'
                keys_chosen.append('z')


    for i in range(len(word)):
        pygame.draw.rect(window, (135, 223, 252), (i * 80, 680, 50, 10))

    if chosen in word and chosen != '':
        correct.append(chosen)
    elif chosen != '':
        wrong += 1
        incorrect.append(chosen)
    for i in correct:
        for j in findOccurrences(word, i):
            gameFont.render_to(window, (80 * j + 10, 640), i, (135, 223, 252))
        guessed = set(correct)
        full_word = set(word)
        if guessed == full_word:
            level += 1
            correct = []
            incorrect = []
            keys_chosen = []
            theme = random.choice(theme_list)
            word = random.choice(theme)
    for i in range(len(incorrect)):
        if i <= 10:
            gameFont.render_to(window, (40 * i + 410, 125), incorrect[i], (135, 223, 252))
        if i > 10:
            gameFont.render_to(window, (40 * i - 430 + 400, 200), incorrect[i], (135, 223, 252))
    pygame.display.update()
