import math
import random

import pygame
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

#Fondo
background = pygame.image.load('fondo.jpg')

# Sonido
mixer.music.load("audio-fondo.mp3")
mixer.music.play(-2)

# Titulo
pygame.display.set_caption("Invasion Zombie")
icon = pygame.image.load('zombies.png')
pygame.display.set_icon(icon)

# Jugador
playerImg = pygame.transform.scale(pygame.image.load('archer.png'), (125, 125))
playerX = 370
playerY = 480
playerX_change = 0

# Enemigos
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
imagen_original = pygame.image.load('zombies.png')
imagen_redimens = pygame.transform.scale(imagen_original, (55, 55))

for i in range(num_of_enemies):
    enemyImg.append(imagen_redimens)
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(20, 150))
    enemyX_change.append(1)
    enemyY_change.append(20)


arrowImg = pygame.transform.scale(pygame.image.load('arrow.png'), (30, 30))
arrowX = 0
arrowY = 480
arrowX_change = 0
arrowY_change = 10
arrow_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_arrow(x, y):
    global arrow_state
    arrow_state = "fire"
    screen.blit(arrowImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, arrowX, arrowY):
    distance = math.sqrt(math.pow(enemyX - arrowX, 2) + (math.pow(enemyY - arrowY, 2)))
    if distance < 27:
        return True
    else:
        return False


def show_menu():
    menu_font = pygame.font.Font('freesansbold.ttf', 64)
    start_text = menu_font.render("Comenzar Juego", True, (0, 0, 0))
    instruction_text = menu_font.render("Instrucciones", True, (0, 0, 0))

    start_rect = start_text.get_rect(center=(400, 300))
    instruction_rect = instruction_text.get_rect(center=(400, 400))

    while True:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_rect.collidepoint(mouse_pos):
                    return
                elif instruction_rect.collidepoint(mouse_pos):
                    show_instructions()

        screen.blit(start_text, start_rect)
        screen.blit(instruction_text, instruction_rect)

        pygame.display.update()


def show_instructions():
    instruction_font = pygame.font.Font('freesansbold.ttf', 20)
    instructions = [
        "Instrucciones:",
        "- Usa las teclas de flecha izquierda y derecha para mover al jugador.",
        "- Presiona la barra espaciadora "
        "para disparar flechas.",
        "- Elimina a los zombis para ganar puntos.",
        "- Si los zombis te alcanzan, pierdes el juego.",
        "",
        "Presiona cualquier tecla "
        "para regresar al menú."
    ]

    instruction_rects = []
    for i, instruction in enumerate(instructions):
        instruction_text = instruction_font.render(instruction, True, (0, 0, 0))
        instruction_rect = instruction_text.get_rect(center=(400, 100 + i * 40))
        screen.blit(instruction_text, instruction_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                return


def game_loop():
    # ...
    while running:
        if game_over:
            # ...
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_over = False
                        score_value = 0
                        playerX = 370
                        playerY = 480
                        playerX_change = 0
                        arrowX = 0
                        arrowY = 480
                        arrow_state = "ready"
                        for i in range(num_of_enemies):
                            enemyX[i] = random.randint(0, 736)
                            enemyY[i] = random.randint(20, 150)

        else:
            # ...
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        playerX_change = -5
                    if event.key == pygame.K_RIGHT:
                        playerX_change = 5
                    if event.key == pygame.K_SPACE:
                        if arrow_state == "ready":
                            arrowSound = mixer.Sound("flecha (1).mp3")
                            arrowSound.play()
                            arrowX = playerX
                            fire_arrow(arrowX, arrowY)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        playerX_change = 0

            playerX += playerX_change

            if playerX <= 0:
                playerX = 0
            elif playerX >= 736:
                playerX = 736

            for i in range(num_of_enemies):
                if enemyY[i] > 440:
                    game_over





# Game Loop
running = True
show_menu()

while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if arrow_state == "ready":
                    arrowSound = mixer.Sound("flecha (1).mp3")
                    arrowSound.play()
                    # Get the current x cordinate of the spaceship
                    arrowX = playerX
                    fire_arrow(arrowX, arrowY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0



    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], arrowX, arrowY)
        if collision:
            explosionSound = mixer.Sound("sonido-zombie.mp3")
            explosionSound.play()
            arrowY = 480
            arrow_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # arrow Movement
    if arrowY <= 0:
        arrowY = 480
        arrow_state = "ready"

    if arrow_state == "fire":
        fire_arrow(arrowX, arrowY)
        arrowY -= arrowY_change

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
