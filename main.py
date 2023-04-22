from turtle import up
import pygame
pygame.init()
WINDOW_WDTH = 800
WINDOW_HGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WDTH,WINDOW_HGHT))
pygame.display.set_caption('Warspear offline')
PLAYER_WDTH = 40
PLAYER_HGHT = 70
PLAYER_VELOCITY = 5
CURSOR_SIZE = 30
clock = pygame.time.Clock()


# draw a single frame
def draw(player, cursor):
    WINDOW.fill('black')
    pygame.draw.circle(WINDOW, (0,255,0), cursor, CURSOR_SIZE, 5)
    pygame.draw.rect(WINDOW, (255,255,255), player)
    pygame.display.update()

def setDestination(x, y, coords: tuple):
    if x != coords[0]:
        print()

#Offset distance by half the player size to player moves to center of cursor
def getDistance(player_coord, coord, x: bool):
    if x:
        return (player_coord+PLAYER_WDTH/2) - coord
    return (player_coord+65) - coord

def movePlayer(player, distance_X, distance_Y):
   #First move X axis, then move Y axis
    if distance_X < 0 and distance_X < PLAYER_VELOCITY:
        player.x += PLAYER_VELOCITY
        distance_X += PLAYER_VELOCITY
    elif distance_X > 0 and distance_X > PLAYER_VELOCITY:
        player.x -= PLAYER_VELOCITY
        distance_X -= PLAYER_VELOCITY
    else:
        if distance_Y < 0 and distance_Y < PLAYER_VELOCITY:
            player.y += PLAYER_VELOCITY
            distance_Y += PLAYER_VELOCITY
        elif distance_Y > 0 and distance_Y > PLAYER_VELOCITY:
            player.y -= PLAYER_VELOCITY
            distance_Y -= PLAYER_VELOCITY
        
    return (distance_X, distance_Y)

def move_with_keys(player):
    #movement test with keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= PLAYER_VELOCITY
    if keys[pygame.K_RIGHT] and player.x < WINDOW_WDTH-PLAYER_WDTH:
        player.x += PLAYER_VELOCITY    

def main():
    destination_X = 0
    destination_Y = 0
    distance_X = 0
    distance_Y = 0
    global moving_X_finished
    moving_X_finished = False
    run = True
    player = pygame.Rect(380, 265, PLAYER_WDTH, PLAYER_HGHT)
    cursor = (60,60)

    # main loop that keeps the game running
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            mouse_coords = pygame.mouse.get_pos()
            cursor = mouse_coords
            if destination_X != mouse_coords[0]:
                destination_X = mouse_coords[0]
                distance_X = getDistance(player.x, destination_X, True)
            if destination_Y != mouse_coords[1]:
                destination_Y = mouse_coords[1]
                distance_Y = getDistance(player.y, destination_Y, False)

        #Move character and update destination
        move = movePlayer(player, distance_X, distance_Y)
        distance_X = move[0]
        distance_Y = move[1]

        clock.tick(30)
        draw(player, cursor)
    
    pygame.quit()

if __name__ == "__main__":
    main()