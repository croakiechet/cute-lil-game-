import pygame

import headsheet
from catframe import CatFrame

pygame.init()
pygame.font.init()

#fonts
dumbcat = pygame.font.Font('fonts/dumbcat.ttf', 40)
main = pygame.font.Font('fonts/main.ttf', 60)
pixel = pygame.font.Font('fonts/pixel.ttf', 60)

pygame.display.set_caption('cute lil game')

#icon
Icon = pygame.image.load('sprites/Julian.png')
pygame.display.set_icon(Icon)

#screen
screen_size = (896, 600)
screen = pygame.display.set_mode(screen_size)

#display
display_text1 = dumbcat.render('dumbcat 40', True, (0, 0, 0))
display_text2 = main.render('main 60', True, (0, 0, 0))
cf = CatFrame('sprites/cat_frame.png')

#heads
head_sheet_image = pygame.image.load('sprites/headsheet.png').convert_alpha()
head_sheet = headsheet.HeadSheet(head_sheet_image)

#rendering
run = True
while run:

    #game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))

    screen.blit(display_text1, (400, 200))
    screen.blit(display_text2, (200, 400))
    screen.blit(cf, (100, 300))

    # show frame image
    screen.blit()
    pygame.display.update()

pygame.quit()