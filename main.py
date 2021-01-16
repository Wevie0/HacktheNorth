import pygame
import pygame.freetype
import random

pygame.init()

window = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Hangbot")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("tech-bg.png")
title = pygame.image.load("title-bg.png")
gameFont = pygame.freetype.Font("Consolas.ttf", 48)

words = ["technology", "boolean", "robot", "computer", "loop", "database", "javascript", "python", "processor", "string",
         "chemistry", "biology", "electron", "neutron", "proton"
         "atom", "cell", "element", "physics", "astronaut", "nebula", "stars", "moon", "satellite", "orbit", "galaxy"]
word = random.choice(words)

level = 0
run = True

images = []
for i in range(7):
    images.append(pygame.image.load("bot%s.png" % str(i+1)))
bot_step = 0


def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


def nextlevel():
    global correct
    global incorrect
    global keys_chosen
    global word
    global level
    global bot_step
    correct = []
    incorrect = []
    keys_chosen = []
    words.remove(word)
    word = random.choice(words)
    level += 1
    bot_step = 0


correct = []
incorrect = []
keys_chosen = []

nxt = False
while run:  # Main Loop
    chosen = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and level == 0:
            cursor = pygame.mouse.get_pos()
            if 675 >= cursor[0] >= 225 and 525 >= cursor[1] >= 315:
                level = 1
        if event.type == pygame.KEYDOWN and level >= 1:
            if event.key == pygame.K_a and 'a' not in keys_chosen:
                chosen = 'a'
                keys_chosen.append('a')
            elif event.key == pygame.K_b and 'b' not in keys_chosen:
                chosen = 'b'
                keys_chosen.append('b')
            elif event.key == pygame.K_c and 'c' not in keys_chosen:
                chosen = 'c'
                keys_chosen.append('c')
            elif event.key == pygame.K_d and 'd' not in keys_chosen:
                chosen = 'd'
                keys_chosen.append('d')
            elif event.key == pygame.K_e and 'e' not in keys_chosen:
                chosen = 'e'
                keys_chosen.append('e')
            elif event.key == pygame.K_f and 'f' not in keys_chosen:
                chosen = 'f'
                keys_chosen.append('f')
            elif event.key == pygame.K_g and 'g' not in keys_chosen:
                chosen = 'g'
                keys_chosen.append('g')
            elif event.key == pygame.K_h and 'h' not in keys_chosen:
                chosen = 'h'
                keys_chosen.append('h')
            elif event.key == pygame.K_i and 'i' not in keys_chosen:
                chosen = 'i'
                keys_chosen.append('i')
            elif event.key == pygame.K_j and 'j' not in keys_chosen:
                chosen = 'j'
                keys_chosen.append('j')
            elif event.key == pygame.K_k and 'k' not in keys_chosen:
                chosen = 'k'
                keys_chosen.append('k')
            elif event.key == pygame.K_l and 'l' not in keys_chosen:
                chosen = 'l'
                keys_chosen.append('l')
            elif event.key == pygame.K_m and 'm' not in keys_chosen:
                chosen = 'm'
                keys_chosen.append('m')
            elif event.key == pygame.K_n and 'n' not in keys_chosen:
                chosen = 'n'
                keys_chosen.append('n')
            elif event.key == pygame.K_o and 'o' not in keys_chosen:
                chosen = 'o'
                keys_chosen.append('o')
            elif event.key == pygame.K_p and 'p' not in keys_chosen:
                chosen = 'p'
                keys_chosen.append('p')
            elif event.key == pygame.K_q and 'q' not in keys_chosen:
                chosen = 'q'
                keys_chosen.append('q')
            elif event.key == pygame.K_r and 'r' not in keys_chosen:
                chosen = 'r'
                keys_chosen.append('r')
            elif event.key == pygame.K_s and 's' not in keys_chosen:
                chosen = 's'
                keys_chosen.append('s')
            elif event.key == pygame.K_t and 't' not in keys_chosen:
                chosen = 't'
                keys_chosen.append('t')
            elif event.key == pygame.K_u and 'u' not in keys_chosen:
                chosen = 'u'
                keys_chosen.append('u')
            elif event.key == pygame.K_v and 'v' not in keys_chosen:
                chosen = 'v'
                keys_chosen.append('v')
            elif event.key == pygame.K_w and 'w' not in keys_chosen:
                chosen = 'w'
                keys_chosen.append('w')
            elif event.key == pygame.K_x and 'x' not in keys_chosen:
                chosen = 'x'
                keys_chosen.append('x')
            elif event.key == pygame.K_y and 'y' not in keys_chosen:
                chosen = 'y'
                keys_chosen.append('y')
            elif event.key == pygame.K_z and 'z' not in keys_chosen:
                chosen = 'z'
                keys_chosen.append('z')
            elif event.key == pygame.K_RETURN and nxt:
                nxt = False
                nextlevel()

    if level == 0:
        window.blit(title, (0, 0))

    if level >= 1:
        window.fill((255,255, 255))
        window.blit(background, (0, 0))
        if bot_step > 0:
            window.blit(images[bot_step-1], (100, 100))
        BLUE = (133, 138, 227)
        PURPLE = (97, 61, 193)
        pygame.draw.rect(window, PURPLE, (390, 90, 470, 170))
        pygame.draw.rect(window, BLUE, (400, 100, 450, 150))
        for i in range(len(word)):
            pygame.draw.rect(window, (135, 223, 252), (i * 80, 680, 50, 10))
        if chosen is None:
            pass
        elif chosen in word and chosen:
            correct.append(chosen)
        else:
            bot_step += 1
            incorrect.append(chosen)
        for i in correct:
            for j in findOccurrences(word, i):
                gameFont.render_to(window, (80 * j + 10, 640), i, (135, 223, 252))
            guessed = set(correct)
            full_word = set(word)
            if guessed == full_word:
                nxt = True
        for i in range(len(incorrect)):
            if i <= 10:
                gameFont.render_to(window, (40 * i + 410, 125), incorrect[i], (135, 223, 252))
            if i > 10:
                gameFont.render_to(window, (40 * i - 430 + 400, 200), incorrect[i], (135, 223, 252))
        gameFont.render_to(window, (850, 650), str(level - 1), (135, 223, 252))
    pygame.display.update()
