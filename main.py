import pygame
from catframe import CatFrame
from button import Button
from textmake import TextMake
import headsheet

# Initialize pygame
pygame.init()
pygame.font.init()

# Create the Screen
screen_size = (800, 600)
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

# Headsheet Cats
ChoseCharacter = False
head_sheet = headsheet.HeadSheet()

black_1 = head_sheet.get_image(0, 256, 256, 0.25)
black_2 = head_sheet.get_image(1, 256, 256, 0.25)
black_3 = head_sheet.get_image(2, 256, 256, 0.25)

blacktabby_1 = head_sheet.get_image(3, 256, 256, 0.25)
blacktabby_2 = head_sheet.get_image(4, 256, 256, 0.25)
blacktabby_3 = head_sheet.get_image(5, 256, 256, 0.25)

calico_1 = head_sheet.get_image(6, 256, 256, 0.25)
calico_2 = head_sheet.get_image(7, 256, 256, 0.25)
calico_3 = head_sheet.get_image(8, 256, 256, 0.25)

grey_1 = head_sheet.get_image(9, 256, 256, 0.25)
grey_2 = head_sheet.get_image(10, 256, 256, 0.25)
grey_3 = head_sheet.get_image(11, 256, 256, 0.25)

greytabby_1 = head_sheet.get_image(12, 256, 256, 0.25)
greytabby_2 = head_sheet.get_image(13, 256, 256, 0.25)
greytabby_3 = head_sheet.get_image(14, 256, 256, 0.25)

orange_1 = head_sheet.get_image(15, 256, 256, 0.25)
orange_2 = head_sheet.get_image(16, 256, 256, 0.25)
orange_3 = head_sheet.get_image(17, 256, 256, 0.25)

orangetabby_1 = head_sheet.get_image(18, 256, 256, 0.25)
orangetabby_2 = head_sheet.get_image(19, 256, 256, 0.25)
orangetabby_3 = head_sheet.get_image(20, 256, 256, 0.25)

white_1 = head_sheet.get_image(21, 256, 256, 0.25)
white_2 = head_sheet.get_image(22, 256, 256, 0.25)
white_3 = head_sheet.get_image(23, 256, 256, 0.25)

# Choose Your Character

# Choose Cats
choose_cat_list = [black_1, blacktabby_1, calico_1, grey_1, greytabby_1, orange_1, orangetabby_1, white_1]

# Cat Frame
catframe = CatFrame(0.75, screen_size)
catframe_pos = (catframe.set_position()[0], catframe.set_position()[1] + 50)

# Title
cyc = TextMake(main_font, "choose your character", (54, 44, 35), screen_size)
cyc_pos = (cyc.set_position()[0], cyc.set_position()[1] - 218)

# Buttons
left_button = Button('sprites/Left.png', 0.65, screen_size)
right_button = Button('sprites/Right.png', 0.65, screen_size)
left_button_pos = (left_button.set_position()[0] - 300, left_button.set_position()[1] + 40)
right_button_pos = (right_button.set_position()[0] + 300, right_button.set_position()[1] + 40)

# Game Loop
run = True
while run:
    screen.fill((255, 255, 255))
    screen.blit(cyc.text_sprite, cyc_pos)

    if ChoseCharacter is False:
        screen.blit(catframe.image, catframe_pos)

    screen.blit(left_button.image, left_button_pos)
    screen.blit(right_button.image, right_button_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            if left_button.rect.collidepoint(pygame.mouse.get_pos()):
                print("left pressed")

    # show frame image
    pygame.display.update()

pygame.quit()
