import pygame

import headsheet

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
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)

#display
display_text1 = dumbcat.render('dumbcat 40', True, (0, 0, 0))
display_text2 = main.render('main 60', True, (0, 0, 0))

#heads
head_sheet_image = pygame.image.load('sprites/headsheet.png').convert_alpha()
head_sheet = headsheet.HeadSheet(head_sheet_image)

black_1 = head_sheet.get_image(0, 256, 256, 0.25, (255, 255, 255))
black_2 = head_sheet.get_image(1, 256, 256, 0.25, (255, 255, 255))
black_3 = head_sheet.get_image(2, 256, 256, 0.25, (255, 255, 255))

#rendering shit
run = True
while run:
    screen.fill((255, 255, 255))

    #game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(display_text1, (400, 200))
    screen.blit(display_text2, (200, 400))
    # show frame image
    screen.blit(black_1, (0, 0))
    screen.blit(black_2, (64, 0))
    screen.blit(black_3, (128, 0))

    pygame.display.update()

pygame.quit()