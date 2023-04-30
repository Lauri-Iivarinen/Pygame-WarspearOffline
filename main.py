
import pygame
from classes.Map_room import Map_room
from classes.Player import Player
from classes.Mob import Mob
from classes.Ability import Ability
from classes.Combat_text import Combat_text
from classes.Quest import Quest

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
combat_txt = []
announcement = []
open_quest=[]

def clear_opened_quest():
    if len(open_quest) > 0:
        open_quest.pop()

def draw_menu():
    WINDOW.fill((145,150,50))
    title = LARGEFONT.render('WARSPER OFFLINE', 1, 'black')
    WINDOW.blit(title, (75,75))
    play_frame = pygame.Rect(75, 130, 100, 50)
    play_txt = BIGFONT.render('PLAY', 1, 'black')
    WINDOW.blit(play_txt, (100,140))
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

def draw_announcement():
    for txt in announcement:
        text = BIGFONT.render(txt.txt, 1, txt.color)
        WINDOW.blit(text, (txt.x, txt.y))
        txt.update_pos(1)#Text velocity
        if txt.lifetime <= 0:
            index = announcement.index(txt)
            announcement.pop(index)

def draw_combat_text():
    for txt in combat_txt:
        text = FONT.render(txt.txt, 1, txt.color)
        WINDOW.blit(text, (txt.x, txt.y))
        txt.update_pos(2)#Text velocity
        if txt.lifetime <= 0:
            index = combat_txt.index(txt)
            combat_txt.pop(index)

def draw_opened_quest(quest: Quest, cursor, player: Player,x: int, y: int, completing_quest, target: Mob):
    bg = pygame.Rect(x,y,280,280)
    pygame.draw.rect(WINDOW, (255,215,128), bg)
    frame = pygame.Rect(x,y,280,280)
    pygame.draw.rect(WINDOW, 'black', frame, 1)
    title = FONT.render(quest.title, 1, 'black')
    WINDOW.blit(title, (x+10,y))
    info_txt = quest.information.split('\n')
    txt_y = y+20
    for txt in info_txt:
        information = SMALLFONT.render(txt, 1, 'black')
        WINDOW.blit(information, (x+10,txt_y))
        txt_y += 10
    object = SMALLFONT.render(quest.object, 1, 'black')
    WINDOW.blit(object, (x+10, 370))
    if completing_quest:
        txt_frame = pygame.Rect(x+10,390,70,40)
        pygame.draw.rect(WINDOW, 'black', txt_frame, 1)
        object = FONT.render('Complete', 1, 'black')
        WINDOW.blit(object, (x+15,400))
    else:
        txt_frame = pygame.Rect(x+10,390,70,40)
        pygame.draw.rect(WINDOW, 'black', txt_frame, 1)
        object = FONT.render('Accept', 1, 'black')
        dcl_frame = pygame.Rect(x+90,390,70,40)
        pygame.draw.rect(WINDOW, 'black', dcl_frame, 1)
        decline = FONT.render('Decline', 1, 'black')
        WINDOW.blit(object, (x+15,400))
        WINDOW.blit(decline, (x+95, 400))
        
def get_quests(target: Mob, player: Player):
    quests = []
    quest_count = 0
    for quest in target.quests:
        if quest.lvl_requirement <= player.level:
            quests.append(quest)
            quest_count += 1
        if quest_count == 3:
            break
    return quests

def accept_quest(player: Player, target: Mob):
    if len(open_quest) == 1:
        if player.accept_quest(open_quest[0]):
            target.quest_accepted(open_quest[0])
            print('QUEST ACCEPTED')
            announcement.append(Combat_text('QUEST ACCEPTED', 'white', 300, 75))
            clear_opened_quest()

def get_completed_quests(target: Mob, player: Player):
    quests = []
    for quest in target.quests_in_process:
        for player_quest in player.quests:
            if quest==player_quest and player_quest.completed:
                quests.append(player_quest)
    return quests

def draw_text_box(target: Mob, player: Player):
    text_x = 260
    text_y = 110
    bg = pygame.Rect(250, 100, 300, 400)
    pygame.draw.rect(WINDOW, (255,215,128), bg)
    frame = pygame.Rect(250, 100, 300, 400)
    pygame.draw.rect(WINDOW, (194, 132, 0), frame, 4)
    completed_quests = get_completed_quests(target, player)

    txt = target.on_speak_text.split('\n')
    for str in txt:
        greeting = FONT.render(str, 1, 'black')
        WINDOW.blit(greeting, (text_x,text_y))
        text_y += 15

    if len(completed_quests) > 0:
        mouse = pygame.mouse.get_pressed()
        y = 10+text_y
        draw_opened_quest(completed_quests[0], (0,0), player, text_x, 10+text_y, True, target)
        if mouse[0]:
            cursor = pygame.mouse.get_pos()
            if cursor[0] >= text_x and cursor[0] <= text_x+280 and cursor[1] >= 450 and cursor[1] <= 500:
                clear_opened_quest()
            if cursor[0] >= text_x+10 and cursor[0] <= text_x+80 and cursor[1] >= 390 and cursor[1] <= 430:#accept button
                player.complete_quest(completed_quests[0])
                announcement.append(Combat_text('Quest completed', 'white', 300, 75))
    else:
        quests = get_quests(target, player)
        #draw_quests(target, text_x, text_y, player)
        cursor = (0,0)
        mouse = pygame.mouse.get_pressed()
        y = 10+text_y
        if mouse[0]:
            cursor = pygame.mouse.get_pos()
            if cursor[0] >= text_x and cursor[0] <= text_x+280 and cursor[1] >= 450 and cursor[1] <= 500:
                clear_opened_quest()
            if cursor[0] >= text_x+90 and cursor[0] <= text_x+160 and cursor[1] >= 390 and cursor[1] <= 430:#decline button
                clear_opened_quest()
            if cursor[0] >= text_x+10 and cursor[0] <= text_x+80 and cursor[1] >= 390 and cursor[1] <= 430:#accept button
                accept_quest(player, target)
        if len(open_quest) == 0:
            for quest in quests:
                if cursor[0] >= text_x and cursor[0] <= text_x+280 and cursor[1]>=y and cursor[1] <= y+50:
                    open_quest.append(quest)
                    break
                frame = pygame.Rect(text_x,y,280,50)
                pygame.draw.rect(WINDOW, 'black', frame, 1)
                object = FONT.render(f'{quest.xp}xp - {quest.title}!', 1, 'black')
                WINDOW.blit(object, (text_x+10, y+10))
                y += 60
        else:
            draw_opened_quest(open_quest[0], (0,0), player, text_x, y, False, target)

def draw_quest_tracker(player: Player):
    text = FONT.render(f'Quests {len(player.quests)}/3:', 1, 'white')
    WINDOW.blit(text, (650, 20))
    x = 660
    y = 40
    for quest in player.quests:
        obj = SMALLFONT.render(quest.object, 1, 'white')
        if quest.completed:
            count = FONT.render('Completed!', 1, 'white')
        else:
            count = FONT.render(f'{quest.current_count}/{quest.object_count}', 1, 'white')
        WINDOW.blit(obj, (x,y))
        WINDOW.blit(count, (x, y+10))
       
        y += 25


# draw a single frame
def draw(player, cursor, cursor_color, player_info: Player, active_target, speaking: bool, accepting_quest=False):
    WINDOW.fill('black')
    if not speaking:
        pygame.draw.circle(WINDOW, cursor_color, cursor, CURSOR_SIZE, CURSOR_THICKNESS) #Cursor
    draw_mobs()
    draw_UI(player_info)
    if active_target:
        draw_target_UI(active_target)
    draw_ability_bar(player_info.abilities)
    draw_combat_text()
    draw_announcement()
    draw_quest_tracker(player_info)
    pygame.draw.rect(WINDOW, (255,255,255), player)#Player model
    if speaking and active_target:
        draw_text_box(active_target, player_info)
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
            combat_txt.append(Combat_text(f'{damage}','white',target.x, target.y))
            player_info.receive_damage(target.damage)
            combat_txt.append(Combat_text(f'{target.damage}','red', player.x, player.y))
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
            clear_opened_quest()
            clock.tick(30)#framerate
            draw(player, cursor, cursor_color, player_info, active_target, speaking) #Draw current frame
        elif not in_menu:#Talking
            mouse = pygame.mouse.get_pressed()
            if mouse[0]:
                cursor = pygame.mouse.get_pos()
                if cursor[0] < 250 or cursor[0] > 550 or cursor[1] < 100 or cursor[1] > 500:
                    speaking = False
                    active_target = False
                    cursor=(-60,-60)
            clock.tick(30)#framerate
            draw(player, cursor, cursor_color, player_info, active_target, speaking)
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