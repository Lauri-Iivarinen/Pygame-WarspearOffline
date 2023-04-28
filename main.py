import pygame
from Map_room import Map_room
from Player import Player
from Mob import Mob
from Ability import Ability

pygame.init()
pygame.font.init()
WINDOW_WDTH = 800 #20x15 movable area
WINDOW_HGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WDTH,WINDOW_HGHT))
pygame.display.set_caption('Warspear offline')
PLAYER_WDTH = 20
PLAYER_HGHT = 50
PLAYER_VELOCITY = 5
CURSOR_SIZE = 20
CURSOR_THICKNESS = 3
FONT = pygame.font.SysFont('comicsans', 15, True, italic=False)
SMALLFONT = pygame.font.SysFont('comicsans', 10, True, italic=False)
BIGFONT = pygame.font.SysFont('comicsans', 20, True, italic=False)
LARGEFONT = pygame.font.SysFont('comicsans', 30, True, italic=False)
clock = pygame.time.Clock()

current_map = Map_room(1)
current_map.print_map()

def draw_menu():
    WINDOW.fill((145,150,50))
    title = LARGEFONT.render('WARSPER OFFLINE', 1, 'black')
    WINDOW.blit(title, (75,75))
    play_frame = pygame.Rect(75, 130, 100, 50)
    play_txt = BIGFONT.render('PLAY', 1, 'black')
    WINDOW.blit(play_txt, (80,135))
    pygame.draw.rect(WINDOW, 'black', play_frame, 1)
    pygame.display.update()

def get_text_pos(x,y,length):
    y -= 22
    x -= length*3
    return (x,y)

def draw_mobs():
    for mob in current_map.mobs:
        if mob.alive:
            npc_name = FONT.render(mob.name, 1, mob.name_color)
            npc_pos = roundCursorPos((mob.x, mob.y))
            npc_name_pos = get_text_pos(npc_pos[0]-10, npc_pos[1], len(mob.name))
            npc = pygame.Rect(npc_pos[0]-10, npc_pos[1], PLAYER_WDTH, PLAYER_HGHT)
            WINDOW.blit(npc_name, npc_name_pos)
            pygame.draw.rect(WINDOW, mob.color, npc)
        else:
            npc_pos = roundCursorPos((mob.x, mob.y))
            npc = pygame.Rect(npc_pos[0]-10, npc_pos[1]+PLAYER_WDTH, PLAYER_HGHT, PLAYER_WDTH)
            pygame.draw.rect(WINDOW, mob.color, npc)

def draw_UI(player: Player):
    ui_frame = pygame.Rect(0,0,150,50)
    name = FONT.render(player.name, 1, 'black')
    pygame.draw.rect(WINDOW, 'grey', ui_frame)
    health_bar_frame = pygame.Rect(1,25, 102, 7)
    pygame.draw.rect(WINDOW, 'black', health_bar_frame)
    health_bar = pygame.Rect(2,26, round((player.curr_health/player.max_health)*100), 5)
    pygame.draw.rect(WINDOW, 'red', health_bar)
    xp_bar_frame = pygame.Rect(1,33, 102, 7)
    pygame.draw.rect(WINDOW, 'black', xp_bar_frame)
    xp_bar = pygame.Rect(2,34, round((player.xp/100)*100), 5)
    pygame.draw.rect(WINDOW, 'yellow', xp_bar)
    pygame.draw.circle(WINDOW, 'black', (128,25), CURSOR_SIZE, CURSOR_THICKNESS)
    level = FONT.render(f'{player.level}', 1, 'black')
    WINDOW.blit(name, (5,5))
    WINDOW.blit(level, (125,15))

def draw_target_UI(player: Mob):
    ui_frame = pygame.Rect(160,0,150,50)
    name = FONT.render(player.name, 1, 'black')
    hp_txt = FONT.render(f'{player.curr_health}/{player.max_health}', 1, 'black')
    pygame.draw.rect(WINDOW, 'grey', ui_frame)
    health_bar_frame = pygame.Rect(161,25, 102, 7)
    pygame.draw.rect(WINDOW, 'black', health_bar_frame)
    health_bar = pygame.Rect(162,26, round((player.curr_health/player.max_health)*100), 5)
    pygame.draw.rect(WINDOW, 'red', health_bar)
    WINDOW.blit(name, (160,5))
    WINDOW.blit(hp_txt, (165, 32))


def draw_ability_bar(abilities: list):
    x = 250
    y = 550
    ui_frame = pygame.Rect(x,y,300,50)
    pygame.draw.rect(WINDOW, 'grey', ui_frame)
    y += 15
    x += 10
    for ability in abilities:
        name = SMALLFONT.render(ability.name, 1, 'black')
        if ability.usable:
            icon = pygame.Rect(x,y,30,30)#Replace with icon
            pygame.draw.rect(WINDOW, (0,0,0) , icon)
        else:
            cd = FONT.render(f'{ability.cooldown_remaining}', 1, 'black')
            icon = pygame.Rect(x,y,30,30)
            pygame.draw.rect(WINDOW, (0,0,0), icon, 1) 
            WINDOW.blit(cd, (x+12, 570))
        WINDOW.blit(name, (x,552))
        x += 50

# draw a single frame
def draw(player, cursor, cursor_color, player_info: Player, active_target):
    WINDOW.fill('black')
    pygame.draw.circle(WINDOW, cursor_color, cursor, CURSOR_SIZE, CURSOR_THICKNESS) #Cursor
    draw_mobs()
    draw_UI(player_info)
    if active_target:
        draw_target_UI(active_target)
    draw_ability_bar(player_info.abilities)
    pygame.draw.rect(WINDOW, (255,255,255), player)#Player model
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

def do_interact(target: Mob, player, player_info: Player):
    if target.alive:
        close = check_player_range((target.x, target.y), (player.x, player.y))
        if close and target.hostile:
            target.receive_damage(player_info.calc_damage())
            player_info.receive_damage(target.damage)
            if target.curr_health == 0:
                print('targed died')
                player_info.gain_xp(target.xp)
        elif close:
            print('speaking')

def main():
    tick = 0
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
    #Abilioties
    gcd_ok = True
    useHeal = False
    useSlash = False

    in_menu = True
    menu_closed = False

    # main loop that keeps the game running
    while checkGameClose():
        if not in_menu:
            mouse = pygame.mouse.get_pressed()
            if mouse[0] and menu_closed: #Left click moves player
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

            if mouse[2] and menu_closed: #Right click interacts/attacks
                cursor = roundCursorPos(pygame.mouse.get_pos())
                target = check_for_mob(cursor)
                if target:
                    active_target = target
                else: active_target = False
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
                
            #ABILITIES
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1] and gcd_ok:
                useHeal = True
                gcd_ok = False
            if keys[pygame.K_2] and gcd_ok:
                useSlash = True
                gcd_ok = False
            
            #Move character and update destination
            move = movePlayer(player, distance_X, distance_Y)
            distance_X = move[0]
            distance_Y = move[1]

            if tick >= 30:
                tick = 0
                menu_closed = True
                player_info.reduce_cooldowns()
                if active_target:
                    do_interact(active_target, player, player_info)
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

            clock.tick(30)#framerate
            draw(player, cursor, cursor_color, player_info, active_target) #Draw current frame
        else:
            #75, 130, 100, 50
            mouse = pygame.mouse.get_pressed()
            if mouse[0]: #Left click moves player
                cursor = pygame.mouse.get_pos()
                if cursor[0] >= 75 and cursor[0] <= 175 and cursor[1] >= 130 and cursor[1] <= 180:
                    in_menu = False
            clock.tick(30)#framerate
            draw_menu()
    #While loop breaks -> Game closes
    pygame.quit()

if __name__ == "__main__":
    main()