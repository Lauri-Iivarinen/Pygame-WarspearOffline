from turtle import up
import pygame
from Map_room import Map_room

pygame.init()
WINDOW_WDTH = 800 #20x15 movable area
WINDOW_HGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WDTH,WINDOW_HGHT))
pygame.display.set_caption('Warspear offline')
PLAYER_WDTH = 20
PLAYER_HGHT = 50
PLAYER_VELOCITY = 5
CURSOR_SIZE = 20
CURSOR_THICKNESS = 3
clock = pygame.time.Clock()

current_map = Map_room()
current_map.print_map()


# draw a single frame
def draw(player, cursor, cursor_color):
    WINDOW.fill('black')
    pygame.draw.circle(WINDOW, cursor_color, cursor, CURSOR_SIZE, CURSOR_THICKNESS)
    pygame.draw.rect(WINDOW, (255,255,255), player)
    pygame.display.update()

def setDestination(x, y, coords: tuple):
    if x != coords[0]:
        print()

def checkGameClose():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

    return True            

#Offset distance by half the player size to player moves to center of cursor
def getDistance(player_coord, coord, x: bool):
    if x:
        return (player_coord+PLAYER_WDTH/2) - coord
    return (player_coord+45) - coord

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

#Round cursor position for closest "grid" in the playable area
def roundCursorPos(cursor: tuple):
    x = round(cursor[0]/40)
    y = round(cursor[1]/40)
    return (x * 40, y * 40)

def move_with_keys(player):
    #movement test with keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= PLAYER_VELOCITY
    if keys[pygame.K_RIGHT] and player.x < WINDOW_WDTH-PLAYER_WDTH:
        player.x += PLAYER_VELOCITY

def move_ok(cursor: tuple, map):
    x = round(cursor[0]/40)
    y = round(cursor[1]/40)
    return map[y][x]

def main():
    destination_X = 0
    destination_Y = 0
    distance_X = 0
    distance_Y = 0
    player = pygame.Rect(380, 265, PLAYER_WDTH, PLAYER_HGHT)
    cursor = (-60,-60) #Initial position of cursor
    red = (255,0,0)
    green = (0,255,0)
    cursor_color = green

    # main loop that keeps the game running
    while checkGameClose():
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            cursor = roundCursorPos(pygame.mouse.get_pos())
            if move_ok(cursor, current_map.map):
                cursor_color = green
                mouse_coords = cursor
                if destination_X != mouse_coords[0]:
                    destination_X = mouse_coords[0]
                    distance_X = getDistance(player.x, destination_X, True)
                if destination_Y != mouse_coords[1]:
                    destination_Y = mouse_coords[1]
                    distance_Y = getDistance(player.y, destination_Y, False)
            else:
                cursor_color=red
        
        #Move character and update destination
        move = movePlayer(player, distance_X, distance_Y)
        distance_X = move[0]
        distance_Y = move[1]

        clock.tick(30)#framerate
        draw(player, cursor, cursor_color) #Draw current frame
    
    #While loop breaks -> Game closes
    pygame.quit()

if __name__ == "__main__":
    main()