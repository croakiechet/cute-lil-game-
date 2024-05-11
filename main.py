import pygame
from catframe import CatFrame
from leftbutton import LeftButton
from rightbutton import RightButton
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


# Makes text easier to move based on it's size
class TextMake:
    def __init__(self, font, text, color):
        self.text = text
        self.font = font
        self.color = color
        self.text_sprite = self.font.render(self.text, True, self.color)
        self.dimensions = self.font.size(text)

    def get_text_size(self):
        return self.dimensions[0], self.dimensions[1]


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
catframe = CatFrame(0.75)
catframe_size = catframe.get_img_size()
starting_frame_x = (center(screen_size, catframe_size[0], catframe_size[1])[0])
starting_frame_y = (center(screen_size, catframe_size[0], catframe_size[1])[1] + 50)

# Title
CYC_Title = TextMake(main_font, "choose your character", (54, 44, 35))
CYC_Title_Size = CYC_Title.get_text_size()
print(CYC_Title_Size)
title_x = (center(screen_size, CYC_Title_Size[0], CYC_Title_Size[1])[0])
title_y = (center(screen_size, CYC_Title_Size[0], CYC_Title_Size[1])[1] - 218)

# Buttons
left_button = LeftButton(0.65)
left_button_size = left_button.get_img_size()
left_button_x = (center(screen_size, left_button_size[0], left_button_size[1])[0] - 300)
left_button_y = (center(screen_size, left_button_size[0], left_button_size[1])[1] + 40)
right_button = RightButton(0.65)
right_button_size = right_button.get_img_size()
right_button_x = (center(screen_size, left_button_size[0], left_button_size[1])[0] + 300)
right_button_y = (center(screen_size, left_button_size[0], left_button_size[1])[1] + 40)

# Game Loop
run = True
while run:
    screen.fill((255, 255, 255))
    screen.blit(CYC_Title.text_sprite, (title_x, title_y))

    if ChoseCharacter is False:
        screen.blit(catframe.image, (starting_frame_x, starting_frame_y))

    screen.blit(left_button.image, (left_button_x, left_button_y))
    screen.blit(right_button.image, (right_button_x, right_button_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # show frame image
    pygame.display.update()

pygame.quit()
