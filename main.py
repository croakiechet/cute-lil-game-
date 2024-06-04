import pygame
from textmake import TextMake
from player import Player
from objects import Objects
from spritesheet import Spritesheet

# Initialize pygame
pygame.init()
pygame.font.init()

# Create the Screen
screen_size = (900, 650)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
# Pygame Caption and Icon
icon = pygame.image.load('sprites/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('cute lil game')
# Fonts
dumb_font = pygame.font.Font('fonts/dumbcat.ttf', 50)
main_font = pygame.font.Font('fonts/main.ttf', 60)
pixel_font_title = pygame.font.Font('fonts/pixel.ttf', 60)

# spritesheets
my_headsheet = Spritesheet('sprites/headsheet.png')
my_spritesheet = Spritesheet('sprites/spritesheet.png')

HeadSheet_Colors = ['Black', 'Black Bicolor', 'Calico', 'Gray', 'Gray Bicolor', 'Orange', 'Orange Tabby', 'White']
HeadSheet = []
cat_choose = 0
for i in HeadSheet_Colors:
    for num in range(3):
        HeadSheet.append(my_headsheet.parse_sprite(i + " " + str(num + 1) + ".png", 2))
print(HeadSheet)


# Centering Function
def center(size_screen, w, h):
    x_centered = (size_screen[0]) / 2 - w / 2
    y_centered = (size_screen[1]) / 2 - h / 2
    return x_centered, y_centered


HeadSheet_pos = (center(screen_size, HeadSheet[cat_choose].get_width(), HeadSheet[cat_choose].get_height())[0],
                 center(screen_size, HeadSheet[cat_choose].get_width(), HeadSheet[cat_choose].get_height())[1] + 20)

# Choose Your Character Scene
# Cat Frame
catframe = Objects('sprites/frame.png', 0.9)
catframe_pos = (catframe.set_position()[0], catframe.set_position()[1] + 30)
# Title
cyc = TextMake(main_font, "choose your character", (54, 44, 35), screen_size)
cyc_pos = (cyc.set_position()[0], cyc.set_position()[1] - 265)
# Buttons
left_button = Objects('sprites/Left.png', 0.8)
right_button = Objects('sprites/Right.png', 0.8)
left_button.rect.topleft = (left_button.set_position()[0] - 330, left_button.set_position()[1] + 25)
right_button.rect.topleft = (right_button.set_position()[0] + 330, right_button.set_position()[1] + 25)
done_button = Objects('sprites/Done.png', 0.55)
done_button.rect.topleft = (done_button.set_position()[0] + 340, done_button.set_position()[1] + 245)
cat_choose = 0
CYCScene = True

# Bedroom Scene
Bedroom = False
Player = Player(0, 0, 4)

index = 0

# Game Loop
run = True
while run:
    clock.tick(60)
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_a | pygame.K_LEFT:
                    Player.facing_left = True
                    Player.state = 'walking'
                    Player.move()

                case pygame.K_d | pygame.K_RIGHT:
                    Player.facing_left = False
                    Player.state = 'walking'
                    Player.move()
                case pygame.K_w | pygame.K_UP | pygame.K_SPACE:
                    if Player.state == 'jumping':
                        Player.time_since_jump_activated = current_time - Player.time_since_last_jump
                    else:
                        Player.time_of_last_jump = current_time
                        Player.time_since_jump_activated = 0
                        Player.time_since_last_jump = 0
                        Player.state = 'jumping'
                case pygame.K_s | pygame.K_DOWN | pygame.K_LSHIFT:
                    Player.state = 'sneaking'

        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_w | pygame.K_UP | pygame.K_SPACE:
                    Player.time_of_jump_deactivate = current_time
                    Player.state = 'landing'
            if Player.state == 'jumping':
                if current_time - Player.time_of_last_jump < 500:
                    Player.state = 'jumping'
                else:
                    Player.time_of_last_jump = 0
                    Player.time_of_jump_deactivate = current_time
                    Player.state = 'landing'
            elif Player.state == 'landing':
                if 1 < Player.time_since_last_jump < 300:
                    Player.time_since_last_jump = current_time - Player.time_of_jump_deactivate
                    Player.state = 'landing'
                else:
                    Player.state = 'idling'
            else:
                Player.state = 'idling'

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if left_button.rect.collidepoint(mouse_pos):
                print("left")
                cat_choose -= 3
                cat_choose = cat_choose % 24

            if right_button.rect.collidepoint(mouse_pos):
                print("right button hit")
                cat_choose += 3
                cat_choose = cat_choose % 24

            if done_button.rect.collidepoint(mouse_pos):
                print("done")
                CYCScene = False
                Bedroom = True

    screen.fill((255, 255, 255))
    if CYCScene:
        screen.blit(cyc.text_sprite, cyc_pos)
        screen.blit(catframe.image, catframe_pos)
        screen.blit(left_button.image, left_button.rect)
        screen.blit(right_button.image, right_button.rect)
        screen.blit(done_button.image, done_button.rect)
        screen.blit(HeadSheet[cat_choose], HeadSheet_pos)

    if Bedroom:
        Player.draw(screen)

    if Player.state == 'landing':
        Player.time_since_last_jump = current_time - Player.time_of_jump_deactivate
        if Player.time_since_last_jump < 200:
            Player.state = 'landing'
        else:
            Player.state = 'idling'
    Player.animate()

    # show frame image
    pygame.display.update()

pygame.quit()
