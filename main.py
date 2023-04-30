
import pygame
from classes.Map_room import Map_room
from classes.Player import Player
from classes.Mob import Mob
from classes.Ability import Ability
from classes.Combat_text import Combat_text
from classes.Quest import Quest
from classes.Drawing import Drawing

pygame.init()
WINDOW_WDTH = 800 #20x15 movable area
WINDOW_HGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WDTH,WINDOW_HGHT))
pygame.display.set_caption('Warspear offline')
PLAYER_WDTH = 20
PLAYER_HGHT = 50
PLAYER_VELOCITY = 5
clock = pygame.time.Clock()

current_map = Map_room(1)
current_map.print_map()
#class for rendering the screen
drawing = Drawing(WINDOW, current_map)

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

def movePlayer(player, distance_X, distance_Y, target, r_click: bool):
    if target and r_click:
        if check_player_range((player.x, player.y), (target.x, target.y)):
            return (distance_X, distance_Y)
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

def map_grid_pos(cursor: tuple):
    x = round(cursor[0]/40)
    y = round(cursor[1]/40)
    return (x,y)

def check_for_mob(coords: tuple):
    pos = map_grid_pos(coords)
    for mob in current_map.mobs:
        mob_pos = map_grid_pos((mob.x, mob.y+PLAYER_HGHT))
        if mob_pos == pos:
            return mob
    return False

def check_player_range(target: tuple, player: tuple) -> bool:
    t = map_grid_pos(target)
    p = map_grid_pos(player)

    if (t[0] - p[0] <= 1 and t[0] - p[0] >= -1):
        if (t[1] - p[1] <= 1 and t[1] - p[1] >= -1):
            return True
    
    return False

def update_quests(player: Player, target=False):
    for quest in player.quests:
        if target:
            print('goblin killed')
            if quest.object_target == target.name:
                quest.update_count()

def do_interact(target: Mob, player, player_info: Player):
    if target.alive:
        close = check_player_range((target.x, target.y), (player.x, player.y))
        if close and target.hostile:
            damage = player_info.calc_damage()
            target.receive_damage(damage)
            drawing.combat_txt.append(Combat_text(f'{damage}','white',target.x, target.y))
            player_info.receive_damage(target.damage)
            drawing.combat_txt.append(Combat_text(f'{target.damage}','red', player.x, player.y))
            if target.curr_health == 0:
                print('targed died')
                update_quests(player_info, target)
                player_info.gain_xp(target.xp)
        elif close:
            return True

    return False

def main():
    tick = 0 #Framerate tick
    #Player movement
    destination_X = 0
    destination_Y = 0
    distance_X = 0
    distance_Y = 0
    player = pygame.Rect(380, 265, PLAYER_WDTH, PLAYER_HGHT)
    cursor = (-60,-60) #Initial position of cursor
    red = (255,0,0)
    green = (0,255,0)
    cursor_color = green
    player_info = Player('Greenmafia', 200, 200, 1, 0, [], []) #PLAYER DATA
    active_target = False
    r_click = False
    speaking = False

    #Abilioties
    gcd_ok = True
    useHeal = False
    useSlash = False

    #MAIN MENU HANDLERS
    in_menu = True
    menu_closed = False

    

    # main loop that keeps the game running
    while checkGameClose():
        if not in_menu and not speaking:
            mouse = pygame.mouse.get_pressed()
            if mouse[0] and menu_closed: #Left click moves player
                cursor = roundCursorPos(pygame.mouse.get_pos())
                if move_ok(cursor, current_map.map):
                    cursor_color = green
                    mouse_coords = cursor
                    r_click = False
                    if destination_X != mouse_coords[0]:
                        destination_X = mouse_coords[0]
                        distance_X = getDistance(player.x, destination_X, True)
                    if destination_Y != mouse_coords[1]:
                        destination_Y = mouse_coords[1]
                        distance_Y = getDistance(player.y, destination_Y, False)
                else:
                    cursor_color=red

            if mouse[2] and menu_closed: #Right click interacts/attacks
                cursor = roundCursorPos(pygame.mouse.get_pos())
                target = check_for_mob(cursor)
                if target:
                    active_target = target
                else: active_target = False
                if move_ok(cursor, current_map.map):
                    cursor_color = green
                    mouse_coords = cursor
                    r_click = True
                    if destination_X != mouse_coords[0]:
                        destination_X = mouse_coords[0]
                        distance_X = getDistance(player.x, destination_X, True)
                    if destination_Y != mouse_coords[1]:
                        destination_Y = mouse_coords[1]
                        distance_Y = getDistance(player.y, destination_Y, False)
                else:
                    cursor_color=red
                
            #ABILITIES
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1] and gcd_ok:
                useHeal = True
                gcd_ok = False
            if keys[pygame.K_2] and gcd_ok:
                useSlash = True
                gcd_ok = False
            
            #Move character and update destination
            move = movePlayer(player, distance_X, distance_Y, active_target, r_click)
            distance_X = move[0]
            distance_Y = move[1]

            if tick >= 30:
                tick = 0
                menu_closed = True
                player_info.reduce_cooldowns()
                if active_target:
                    speaking = do_interact(active_target, player, player_info)
                if useHeal:
                    player_info.useAbility('Vitalize')
                    useHeal = False
                    gcd_ok = True
                if useSlash:
                    player_info.useAbility('Slash')
                    useSlash = False
                    gcd_ok = True
                
            else:
                tick += 1
            drawing.clear_opened_quest()
            clock.tick(30)#framerate
            drawing.draw(player, cursor, cursor_color, player_info, active_target, speaking) #Draw current frame
        elif not in_menu:#Talking
            mouse = pygame.mouse.get_pressed()
            if mouse[0]:
                cursor = pygame.mouse.get_pos()
                if cursor[0] < 250 or cursor[0] > 550 or cursor[1] < 100 or cursor[1] > 500:
                    speaking = False
                    active_target = False
                    cursor=(-60,-60)
            clock.tick(30)#framerate
            drawing.draw(player, cursor, cursor_color, player_info, active_target, speaking)
        else:
            #75, 130, 100, 50
            mouse = pygame.mouse.get_pressed()
            if mouse[0]: #Left click moves player
                cursor = pygame.mouse.get_pos()
                if cursor[0] >= 75 and cursor[0] <= 175 and cursor[1] >= 130 and cursor[1] <= 180:
                    in_menu = False
            clock.tick(30)#framerate
            drawing.draw_menu()
    #While loop breaks -> Game closes
    pygame.quit()

if __name__ == "__main__":
    main()