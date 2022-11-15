import pygame
import button
from pygame import mixer

pygame.init()

# create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load("img/background.jpg")
pygame.display.set_caption("Main Menu")

# game variables
game_paused = False
menu_state = "main"
algorithm = ""

# define fonts
font = pygame.font.SysFont("comicsansms", 40)

# define mixer to play music
mixer.init()
# music
main_music = pygame.mixer.Sound('music/main_theme.ogg')
# sounds
select_sound = pygame.mixer.Sound('sounds/bump.ogg')

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


# create button instances
start_button = button.Button(SCREEN_WIDTH/2, 125, start_img, 1)
algorithm_button = button.Button(SCREEN_WIDTH/2, 250, algorithm_img, 1)
quit_button = button.Button(SCREEN_WIDTH/2, 375, quit_img, 1)
informed_button = button.Button(SCREEN_WIDTH/2, 75, informed_img, 1)
uninformed_button = button.Button(SCREEN_WIDTH/2, 200, uninformed_img, 1)
amplitude_button = button.Button(SCREEN_WIDTH/2, 75, amplitude_img, 1)
cost_button = button.Button(SCREEN_WIDTH/2, 200, cost_img, 1)
depth_button = button.Button(SCREEN_WIDTH/2, 325, depth_img, 1)
greedy_button = button.Button(SCREEN_WIDTH/2, 75, greedy_img, 1)
aStar_button = button.Button(SCREEN_WIDTH/2, 200, aStar_img, 1)
"""keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)
"""


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)

    screen.blit(img, (400-img.get_width()/2, y))


# game loop
run = True
while run:

    screen.fill((52, 78, 91))
    screen.blit(bg, (0, 0))

    # check if game is paused
    if game_paused == True:
        # check menu state
        if menu_state == "main":
            draw_text("Search BY " + algorithm, font, TEXT_COL, 400, 70)
            # draw pause screen buttons
            if start_button.draw(screen, SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)
                game_paused = False
            if algorithm_button.draw(screen, SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)
                menu_state = "algorithms"
            if quit_button.draw(screen, SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)
                run = False

        # check if the algorithms menu is open
        if menu_state == "algorithms":
            # draw the different algorithms buttons
            if informed_button.draw(screen, SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)
                print("informed")
                menu_state = "informed"
            if uninformed_button.draw(screen, SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)
                print("uninformed")
                menu_state = "uninformed"
        if menu_state == "informed":
            if amplitude_button.draw(screen, SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)
                print("amplitude")
                algorithm = "amplitude"
                menu_state = "main"
            if cost_button.draw(screen, SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)
                print("cost")
                algorithm = "cost"
                menu_state = "main"
            if depth_button.draw(screen, SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)
                print("depth")
                algorithm = "depth"
                menu_state = "main"
        if menu_state == "uninformed":
            if greedy_button.draw(screen, SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)
                print("greedy")
                algorithm = "greedy"
                menu_state = "main"
            if aStar_button.draw(screen, SCREEN_WIDTH):
                pygame.mixer.Sound.play(select_sound)
                print("aStar")
                algorithm = "A*"
                menu_state = "main"

    else:
        draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
