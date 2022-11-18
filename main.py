import pygame
import button
from pygame import mixer
import controller as control
import sys
import math
import numpy as np
import time
import random

pygame.init()

# create game window
# main menu size
MENU_SCREEN_WIDTH = 800
MENU_SCREEN_HEIGHT = 600

# game size
GAME_SCREEN_HEIGHT = 600
GAME_SCREEN_WIDTH = 600

# Grid
BLOCK_SIZE = math.floor(GAME_SCREEN_WIDTH/10)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Main menu screen
# game screen
screen = pygame.display.set_mode((MENU_SCREEN_WIDTH, MENU_SCREEN_HEIGHT))

bg = pygame.image.load("img/background.jpg")
pygame.display.set_caption("Main Menu")

# game variables
game_paused = False
menu_state = "main"
algorithm = ""
game_ended = False
lastState = []
star_effect = 0
bullets = 0

# define fonts
font = pygame.font.SysFont("comicsansms", 40)
font2 = pygame.font.SysFont("comicsansms", 15, True)

# define mixer to play music
mixer.init()
# music
main_music = pygame.mixer.Sound('music/main_theme.ogg')
main_music.set_volume(0)
stage_clear_music = pygame.mixer.Sound('music/stage_clear.wav')
stage_clear_music.set_volume(0)
invincible_music = pygame.mixer.Sound('music/invincible.ogg')
invincible_music.set_volume(0)
# sounds
select_sound = pygame.mixer.Sound('sounds/bump.ogg')
bigJump_sound = pygame.mixer.Sound('sounds/big_jump.ogg')
bigJump_sound.set_volume(0.4)
smallJump_sound = pygame.mixer.Sound('sounds/small_jump.ogg')
smallJump_sound.set_volume(0.4)
hoo_sound = pygame.mixer.Sound('sounds/hoo.wav')
hoo_sound.set_volume(0.4)
hooHoo_sound = pygame.mixer.Sound('sounds/hoohoo.wav')
hooHoo_sound.set_volume(0.4)
waha_sound = pygame.mixer.Sound('sounds/waha.wav')
waha_sound.set_volume(0.4)
yippee_sound = pygame.mixer.Sound('sounds/yippee.wav')
yippee_sound.set_volume(0.4)
yippee_sound = pygame.mixer.Sound('sounds/yippee.wav')
yippee_sound.set_volume(0.4)
jumps = [bigJump_sound, smallJump_sound, hoo_sound,
         hooHoo_sound, waha_sound, yippee_sound]

# Events
oof_sound = pygame.mixer.Sound('sounds/oof.wav')
oof_sound.set_volume(1)
yoshi_sound = pygame.mixer.Sound('sounds/yoshi.wav')
yoshi_sound.set_volume(1)
mario_hurt_sound = pygame.mixer.Sound('sounds/mario_hurt.wav')
mario_hurt_sound.set_volume(0.5)
thwomp_sound = pygame.mixer.Sound('sounds/thwomp.wav')
thwomp_sound.set_volume(1)
fireball_sound = pygame.mixer.Sound('sounds/fireball.ogg')
fireball_sound.set_volume(1)
powerUp_sound = pygame.mixer.Sound('sounds/powerup.ogg')
powerUp_sound.set_volume(1)


hurts = [mario_hurt_sound, oof_sound]
# background music theme
pygame.mixer.Sound.play(main_music)


# define colours
TEXT_COL = (255, 255, 255)

# load button images
start_img = pygame.image.load("img/start.png").convert_alpha()
algorithm_img = pygame.image.load("img/algorithm.png").convert_alpha()
quit_img = pygame.image.load("img/quit.png").convert_alpha()
informed_img = pygame.image.load("img/informed.png").convert_alpha()
amplitude_img = pygame.image.load("img/amplitude.png").convert_alpha()
cost_img = pygame.image.load("img/cost.png").convert_alpha()
depth_img = pygame.image.load("img/depth.png").convert_alpha()
uninformed_img = pygame.image.load("img/uninformed.png").convert_alpha()
greedy_img = pygame.image.load("img/greedy.png").convert_alpha()
aStar_img = pygame.image.load("img/aStar.png").convert_alpha()
back_img = pygame.image.load("img/back.png").convert_alpha()
super_mario_img = pygame.image.load("img/SuperMario.png").convert_alpha()
game_background = pygame.image.load("img/gameBackground.jpg").convert_alpha()


# create button instances
start_button = button.Button(MENU_SCREEN_WIDTH/2, 125, start_img, 1)
algorithm_button = button.Button(MENU_SCREEN_WIDTH/2, 250, algorithm_img, 1)
quit_button = button.Button(MENU_SCREEN_WIDTH/2, 375, quit_img, 1)
informed_button = button.Button(MENU_SCREEN_WIDTH/2, 75, informed_img, 1)
uninformed_button = button.Button(MENU_SCREEN_WIDTH/2, 200, uninformed_img, 1)
amplitude_button = button.Button(MENU_SCREEN_WIDTH/2, 75, amplitude_img, 1)
cost_button = button.Button(MENU_SCREEN_WIDTH/2, 200, cost_img, 1)
depth_button = button.Button(MENU_SCREEN_WIDTH/2, 325, depth_img, 1)
greedy_button = button.Button(MENU_SCREEN_WIDTH/2, 75, greedy_img, 1)
aStar_button = button.Button(MENU_SCREEN_WIDTH/2, 200, aStar_img, 1)
back_button = button.Button(MENU_SCREEN_WIDTH/2, 550, back_img, 1)
"""keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)
"""


def draw_text(text, font, text_col, x, y):

    if algorithm == "" and game_paused:
        img = font.render(
            "Debe seleccionar un algoritmo", True, text_col)
    else:
        img = font.render(text, True, text_col)
    screen.blit(img, (400-img.get_width()/2, y))


def report_text(text, y):

    txt = font2.render(str(text), False, "BLACK")  # "text", antialias, color
    screen.blit(txt, (700-txt.get_width()/2, y))


# game loop
run = True
while run:

    if not game_ended:

        screen.fill((52, 78, 91))
        screen.blit(bg, (0, 0))

    # check if game is paused
    if game_paused == True:
        # check menu state
        if menu_state == "main":
            draw_text("Search BY " + algorithm, font, TEXT_COL, 400, 70)
            # draw pause screen buttons
            if start_button.draw(screen, MENU_SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)
                if algorithm == "":
                    draw_text("Debe seleccionar un algoritmo",
                              font, TEXT_COL, 400, 70)
                else:
                    menu_state = "in_game"

            if algorithm_button.draw(screen, MENU_SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)
                menu_state = "algorithms"
            if quit_button.draw(screen, MENU_SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)
                run = False

        # check if the algorithms menu is open
        if menu_state == "algorithms":
            # draw the different algorithms buttons
            if informed_button.draw(screen, MENU_SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)

                menu_state = "informed"
            if uninformed_button.draw(screen, MENU_SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)

                menu_state = "uninformed"
        if menu_state == "informed":
            if amplitude_button.draw(screen, MENU_SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)

                algorithm = "amplitud"
                menu_state = "main"
            if cost_button.draw(screen, MENU_SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)

                algorithm = "costo uniforme"
                menu_state = "main"
            if depth_button.draw(screen, MENU_SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)

                algorithm = "profundidad"
                menu_state = "main"
        if menu_state == "uninformed":
            if greedy_button.draw(screen, MENU_SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)

                algorithm = "avara"
                menu_state = "main"
            if aStar_button.draw(screen, MENU_SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)

                algorithm = "A*"
                menu_state = "main"
        if menu_state == "in_game":
            # search solution using algorithm selected

            if not game_ended:
                screen.blit(game_background, (GAME_SCREEN_WIDTH, 0))
                screen.blit(super_mario_img, (GAME_SCREEN_WIDTH-18, 10))
                controller = control.Controller(algorithm)
                controller.search()
                solution = controller.getSolution()
                report_text("Profundidad:", 160)
                report_text(controller.getDepth(), 185)
                report_text("Nodos Generados:", 220)
                report_text(controller.getGeneratedNodes(), 245)
                report_text("Nodos Expandidos:", 280)
                report_text(controller.getExpandedNodes(), 305)
                report_text("Costo:", 340)
                report_text(controller.getCost(), 365)
                report_text("Tiempo en S:", 400)
                report_text(controller.getAlgorithmTime()+"s", 425)
                # draw Solution

                startGame(solution)
                game_ended = True
                #menu_state = "end_game"
            # if menu_state == "end_game":
                # print("ended")

            if back_button.draw(screen, 1400):
                game_ended = False
                menu_state = "main"
                main_music.set_volume(0.7)
                pygame.mixer.Sound.stop(invincible_music)
                pygame.mixer.Sound.stop(stage_clear_music)

    else:
        draw_text("Presione espacio para iniciar", font, TEXT_COL, 160, 250)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    def startGame(solution):
        stateAccum = 0
        for state in solution:
            time.sleep(0.8)
            # play random jump sound
            pygame.mixer.Sound.play(random.choice(jumps))
            # clean board
            screen.fill(WHITE, rect=(
                0, 0, GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT))
            # re-draw board
            figures(screen, state, stateAccum)
            stateAccum += 1
            # re-draw grid
            drawGrid(screen)

            for event in pygame.event.get():  # registrar lo que sucede en la ventana
                # print(event)
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.update()

    def drawGrid(screen):

        for x in range(0, GAME_SCREEN_WIDTH, BLOCK_SIZE):
            for y in range(0, GAME_SCREEN_HEIGHT, BLOCK_SIZE):
                rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(screen, BLACK, rect, 1)

    def figures(screen, state, accum):
        global lastState
        global star_effect
        global bullets

        if star_effect == 0:
            main_music.set_volume(0.7)
            pygame.mixer.Sound.stop(invincible_music)

        aux = np.nditer(state, flags=['multi_index'])
        for element in aux:

            if element != 0:
                fig = pygame.image.load("img/%d.jpg" % int(element)).convert()
                if element == 2:
                    if bullets > 0:
                        fig = pygame.image.load(
                            "img/%dfire.jpg" % int(element)).convert()
                    if star_effect > 0:
                        print("STAR:", star_effect)
                        fig = pygame.image.load(
                            "img/%dstar.jpg" % int(element)).convert()
                # Using blit to copy content from one surface to other
                screen.blit(
                    fig, (aux.multi_index[1]*BLOCK_SIZE+5, aux.multi_index[0]*BLOCK_SIZE+5))

            # check sounds and music
            if element == 2 and accum > 0:
                if lastState[aux.multi_index[0]][aux.multi_index[1]] == 5:
                    # sound with star effect
                    if star_effect > 0:
                        pygame.mixer.Sound.play(thwomp_sound)
                    # sound with flower bullets
                    if bullets > 0:
                        bullets -= 1
                        pygame.mixer.Sound.play(fireball_sound)
                    # sound without star effect
                    else:
                        pygame.mixer.Sound.play(random.choice(hurts))
                if lastState[aux.multi_index[0]][aux.multi_index[1]] == 6:
                    pygame.mixer.Sound.play(yoshi_sound)
                    main_music.set_volume(0)
                    pygame.mixer.Sound.play(stage_clear_music)
                if lastState[aux.multi_index[0]][aux.multi_index[1]] == 3 and bullets == 0:
                    pygame.mixer.Sound.stop(invincible_music)
                    pygame.mixer.Sound.play(invincible_music)
                    main_music.set_volume(0)
                    star_effect += 7
                if lastState[aux.multi_index[0]][aux.multi_index[1]] == 4 and star_effect == 0:
                    pygame.mixer.Sound.play(powerUp_sound)
                    bullets += 1

        if star_effect > 0:
            star_effect -= 1
        lastState = state

    pygame.display.update()

pygame.quit()
