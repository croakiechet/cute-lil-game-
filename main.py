import pygame
from button import Button
from textmake import TextMake
from headsheet import HeadSheet
from player import Player
from objects import Objects


# Initialize pygame
pygame.init()
pygame.font.init()

# Create the Screen
screen_size = (900, 650)
screen = pygame.display.set_mode(screen_size)
# Pygame Caption and Icon
icon = pygame.image.load('sprites/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('cute lil game')
# Fonts
dumb_font = pygame.font.Font('fonts/dumbcat.ttf', 50)
main_font = pygame.font.Font('fonts/main.ttf', 60)
pixel_font_title = pygame.font.Font('fonts/pixel.ttf', 60)


# Centering Function
def center(size_screen, w, h):
    x_centered = (size_screen[0]) / 2 - w / 2
    y_centered = (size_screen[1]) / 2 - h / 2
    return x_centered, y_centered


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

# Choose Your Character Scene
cat_choose = 0
CYCScene = True
headsheet = HeadSheet('sprites/headsheet.png', screen_size)
cycat = headsheet.get_image(cat_choose, 256, 256, 1.8)
cycat_pos = (center(screen_size, cycat.get_width(), cycat.get_height())[0], center(screen_size, cycat.get_width(), cycat.get_height())[1] + 20)

# Bedroom Scene
Bedroom = False
center = center(screen_size, 40, 40)

# Game Loop
run = True
while run:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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
        screen.blit(headsheet.get_image(cat_choose, 256, 256, 1.8), cycat_pos)
    # show frame image
    pygame.display.update()

pygame.quit()
