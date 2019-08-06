from classes import *
from Stan2 import *

def scoot(wall,tank):           # Bountry check with tanks and walls and scoots them in the right direction if tank comes in contact
                                #Each tank is split up by an 'X' with 4 quadrants, simplifing the boundry check
    Dx = tank.cent.x - wall.cent.x
    Dy = tank.cent.y - wall.cent.y

    if Dx == 0 :
       return

    slope = Dy/Dx

    upleft = (wall.ycoor - wall.cent.y) / (wall.xcoor - wall.cent.x)
    upright = (wall.ycoor - wall.cent.y) / (wall.xcoor + wall.width - wall.cent.x)
    loright = (wall.ycoor + wall.height - wall.cent.y) / ( wall.xcoor + wall.width - wall.cent.x)
    loleft = (wall.ycoor + wall.height - wall.cent.y) / (wall.xcoor - wall.cent.x)

    if (tank.cent.x < wall.cent.x) and (tank.cent.y < wall.cent.y): #top left of wall
        if slope < upleft:
            tank.x_coord = wall.xcoor - tank.width
        else:
            tank.y_coord = wall.ycoor - tank.height

    elif (tank.cent.x > wall.cent.x) and (tank.cent.y < wall.cent.y): #top right of wall
        if slope > upright:
            tank.x_coord = wall.xcoor + wall.width
        else:
            tank.y_coord = wall.ycoor - tank.height
    elif (tank.cent.x < wall.cent.x) and (tank.cent.y >= wall.cent.y):  # top left of wall
        if slope > loleft:
            tank.x_coord = wall.xcoor - tank.width
        else:
            tank.y_coord = wall.ycoor + wall.height
    else:                                                              # top  right of wall
        if slope < loright:
            tank.x_coord = wall.xcoor + wall.width
        else:
            tank.y_coord = wall.ycoor + wall.height



def b_bounce(tank,wall,x):          #Bounces Bullet off of walls in the correct way
                                    #each bullet is divided similarly as in 'scoot'
    Dx = tank.bxy[x].x - wall.cent.x
    Dy = tank.bxy[x].y - wall.cent.y

    if Dx == 0:
        return

    slope = Dy / Dx

    upleft = (wall.ycoor - wall.cent.y)/(wall.xcoor - wall.cent.x)
    upright = (wall.ycoor - wall.cent.y)/(wall.xcoor + wall.width - wall.cent.x)
    loright = (wall.ycoor + wall.height - wall.cent.y)/(wall.xcoor + wall.width - wall.cent.x)
    loleft = (wall.ycoor + wall.height - wall.cent.y)/(wall.xcoor - wall.cent.x)

    if (tank.bxy[x].x < wall.cent.x) and (tank.bxy[x].y < wall.cent.y):  # top left of wall
        if (slope > upleft):
            tank.bxy[x].y = wall.ycoor-1
            tank.dir[x].y = -tank.dir[x].y
            tank.fuse[x] += 1
        else:
            tank.bxy[x].x = wall.xcoor
            tank.dir[x].x = -tank.dir[x].x
            tank.fuse[x] += 1

    elif (tank.bxy[x].x > wall.cent.x) and (tank.bxy[x].y < wall.cent.y):  # top right of wall
        if (slope < upright):
            tank.bxy[x].y = wall.ycoor + 1
            tank.dir[x].y = -tank.dir[x].y
            tank.fuse[x] += 1
        else:
            tank.bxy[x].x = wall.xcoor + wall.width + 1
            tank.dir[x].x = -tank.dir[x].x
            tank.fuse[x] += 1

    elif (tank.bxy[x].x < wall.cent.x) and (tank.bxy[x].y >= wall.cent.y):  # bot left of wall
        if slope > loleft:
            tank.bxy[x].x = wall.xcoor - 1
            tank.dir[x].x = -tank.dir[x].x
            tank.fuse[x] += 1
        else:
            tank.bxy[x].y = wall.ycoor + wall.height
            tank.dir[x].y = -tank.dir[x].y
            tank.fuse[x] += 1

    else:  # bot right of wall
        if slope > loright:
            tank.bxy[x].y = wall.ycoor + wall.height + 1
            tank.dir[x].y = -tank.dir[x].y
            tank.fuse[x] += 1
        else:
            tank.bxy[x].x = wall.xcoor + wall.width + 1
            tank.dir[x].x = -tank.dir[x].x
            tank.fuse[x] += 1

def bumper(a,b):
    Dx = a.cent.x - b.cent.x
    Dy = a.cent.y - b.cent.y

    if Dx == 0:
        return

    slope = Dy / Dx

    upleft = (b.y_coord - b.cent.y) / (b.x_coord - b.cent.x)
    upright = (b.y_coord - b.cent.y) / (b.x_coord + b.width - b.cent.x)
    loright = (b.y_coord + b.height - b.cent.y) / (b.x_coord + b.width - b.cent.x)
    loleft = (b.y_coord + b.height - b.cent.y) / (b.x_coord - b.cent.x)

    if (a.cent.x < b.cent.x) and (a.cent.y < b.cent.y): #top left of wall
        if slope < upleft:
            a.x_coord = b.x_coord - a.width
        else:
            a.y_coord = b.y_coord - a.height

    elif (a.cent.x > b.cent.x) and (a.cent.y < b.cent.y): #top right of b
        if slope > upright:
            a.x_coord = b.x_coord + b.width
        else:
            a.y_coord = b.y_coord - a.height
    elif (a.cent.x < b.cent.x) and (a.cent.y >= b.cent.y):  # top left of b
        if slope > loleft:
            a.x_coord = b.x_coord - a.width
        else:
            a.y_coord = b.y_coord + b.height
    else:                                                              # top  right of b
        if slope < loright:
            a.x_coord = b.x_coord + b.width
        else:
            a.y_coord = b.y_coord + b.height








def collisions(tanklist, lvlList): # this function operates all of the logic needed for proper collisions
    for i in tanklist:
        for j in tanklist:

            if i != j:
                if i.area.colliderect(j.area):
                    bumper(j,i)

            for x in range(j.clip):
                if j.active[x]:
                    if pygame.Rect.collidepoint(i.area, j.bxy[x]): #player shoots another
                        if j.__class__ != smart:
                            for h in range(j.clip):
                                j.active[h] = False
                                j.bxy[h].x = 0
                                j.bxy[h].y = 0
                            upgrade_gt2st(j)

                        kill_tank(tanklist,i)

                        print("Tank Number : " + str(i.ID) + "\nMet a terrible fate")
                        return lvl
                    for k in range(i.clip):
                        if j.bxy[x] == i.bxy[k] and x != k:
                            j.active[x] = False
                            i.active[k] = False



        for k in lvlList[lvl.value]:                                   #In each level if bullet collides with wall
            for x in range(i.clip):
                if i.active[x] == True:
                    if pygame.Rect.collidepoint(k.area, i.bxy[x]):  # bullet hits wall
                        # print(k.xcoor)
                        b_bounce(i,k,x)         #Function that bounces the bullet properly after wall is hit
                        if i.fuse[x] > i.fuse_val:
                            i.fuse[x] = 0
                            i.bxy[x].x = 0
                            i.bxy[x].y = 0
                            i.active[x] = False


        for k in lvlList[lvl.value]:          #In each level if tank collides with wall
            ind = i.area.colliderect(k.area)
            if ind == False:
                continue
            scoot(k, i)


# converts a general tank to a smart tank type
def upgrade_gt2st(gen_tank):
    if gen_tank.__class__ == Tank_gen:
        gen_tank.__class__= smart
    return


def Startscreen():#Start Screen for user
    pygame.mouse.set_visible(True)
    draw_text(WIN, "Canisters!", 64, win_len / 2, win_ht / 4)
    draw_text(WIN, "WASD = movement, mouse to Aim and Fire", 22, win_len / 2, win_ht / 2)
    draw_text(WIN, "Coded by Dan and Stan", 22, win_len / 2 , win_ht / 2 + 20)
    draw_text(WIN, "Press a key to begin", 18, win_len / 2, win_ht * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                waiting = False
                pygame.mouse.set_visible(False)



# kills a tank and removes it from the tanks list but if player is killed, the game finishes
def kill_tank(tank_list, i ):
    for temp_tank in tank_list:
        if temp_tank.brain == TankBrain.PC:
            if temp_tank.ID == i.ID:
                restart()
                return

    tank_list.remove(i)

# spawns a new ai controlled tank and adds it to the list of all tanks
def spawn_tank(tank_list,level):
    for i in range(0,level):
        Tank_gen._ID += 1
        x = random.uniform(10, win_len - 100)
        y = random.randint(10, win_ht - 100)

        while(1):

            if abs(tank_list[0].x_coord -  x) < 400:
                x = random.uniform(10, win_len - 100)
            elif abs(tank_list[0].y_coord - y) < 200:
                y = random.uniform(10, win_ht - 100)
            else:
                break
        temp = Tank_gen(TankBrain.COM,x,y,random.randint(30,90),random.randint(30,90),4,2,1,red,yellow,yellow,red,2)
        special = random.randint(0,1000)
        if special == 999: #one in 50 ai are special tanks
            temp.__class__= smart
        tank_list.append(temp)

class level:
    value = 0
    def reset_value(self):
        self.value = 0

# runs all the functions needed for the tanks to work
def run_tank(tanklist):

    for temp_tank in tanklist:  #  temp_tank is the tank within tanklist.
                                #  Meaning it will serve as the object representation within the scope of this function
        # dictates the control function of each tank
        if temp_tank.brain == TankBrain.PC:
            temp_tank.pc_control()

        elif temp_tank.brain == TankBrain.COM:
            temp_tank.ai_control(tanklist)
        # bullet mechanics
        temp_tank.gun()
        if temp_tank.__class__ == smart:
            temp_tank.new_bullets()
        temp_tank.display()

    # death logic
    collisions(tanklist, activelvl)
    return

def restart():
    lvl.value = 0

    Startscreen()
    List_of_tanks.clear()
    pc_tank = Tank_gen(TankBrain.PC, 400, 400, 50, 50, 3, 5, 1, blue, white, blue, white, 4)
    List_of_tanks.append(pc_tank)
    spawn_tank(List_of_tanks, 1)
    print(lvl.value)





# template to fill out a new tank baisically
# Tank_gen(xcoord,ycoord,width,height,tankvel,clipsize,fuse,body_c,barrel_c,reticle_c,barrel_len,bullet_c,bullet_spd)

List_of_tanks = []

lvl = level       #Initial Start Screen for user
#intialization nonsense
restart()

while True:
    # control's game's speed/D
    pygame.time.delay(13)
    # erases window for the next update /D
    WIN.fill((1, 1, 1))

    if List_of_tanks.__len__() <= 1 and List_of_tanks[0].brain == TankBrain.PC:
        lvl.value +=1
        List_of_tanks[0].__class__ = Tank_gen
        List_of_tanks[0].body_c = blue
        List_of_tanks[0].fuse_val = 1
        spawn_tank(List_of_tanks,lvl.value)
        for j in List_of_tanks:  #For loop that will remove all the bullets on screen once the player goes the the next level
            for x in range(j.clip):
                j.active[x] = False
    #controls which level is currently loaded
    lvl_Logic(lvl.value)
    # functions that make all of the tanks operate
    run_tank(List_of_tanks)

    # updates screen
    pygame.display.update()


#
