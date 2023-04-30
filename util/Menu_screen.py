import pygame
pygame.font.init()
FONT = pygame.font.SysFont('comicsans', 35, True, italic=False)

def draw():
    WINDOW_WDTH = 800 #20x15 movable area
    WINDOW_HGHT = 600
    WINDOW = pygame.display.set_mode((WINDOW_WDTH,WINDOW_HGHT))
    WINDOW.fill((145,150,50))

    title = FONT.render('WARSPER OFFLINE', 1, 'black')

    WINDOW.blit(title, (50,50))


def menu_screen():
    mouse = pygame.mouse.get_pressed()
    if mouse[0]: #Left click moves player
        cursor = pygame.mouse.get_pos()
        if cursor.x >= 30:
            return False
    draw()
    return True