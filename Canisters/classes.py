from misc import *
from Stan2 import *
import sys


class TankBrain(Enum): #data type for the different methods of control
    PC = 0
    COM = 1


def myslope(x0, y0, x1, y1): #function to return the slope of 2 points
    x2 = x1 - x0
    y2 = y1 - y0
    return x2, y2


class Tank_gen:
    _ID = 0
    def __init__(self, brain = TankBrain.COM, x_coord = random.randrange(100,win_len-100) , y_coord = random.randrange(100,win_len-100), width = 50, height = 50, vel = 2, clip = 1, fuse = 1, body_c = yellow, barrel_c = aqua, reticle_c = aqua, bullet_c = green,bullet_spd = 2):
        self.brain = brain
        self.x_coord = x_coord
        self.y_coord = y_coord

        self.width = width
        self.height = height
        self.area = pygame.Rect(self.x_coord, self.y_coord, self.width, self.height)
        self.vel = vel
        self.reticle = pygame.math.Vector2()
        # Bullet stuffs
        self.cent = pygame.math.Vector2()
        self.barrel = pygame.math.Vector2()
        self.clip = clip
        self.body_c = body_c
        self.barrel_c = barrel_c
        self.reticle_c = reticle_c
        if self.height > self.width:#makes the barrel length proportunal to the tank's body
            self.barrel_len = self.height/2 + 15
        else:
            self.barrel_len = self.width/2 + 15
        #ai speciifc
        self.timer = 50
        self.i = 0
        #bullet stuffs
        self.fuse_val = fuse
        self.bullet_c = bullet_c
        self.bullet_spd = bullet_spd
        self.bxy = []
        self.bxy_prev = []
        self.dir = []
        self.tail = []
        self.active = []
        self.firing = []
        self.fuse = []
        self.stun = []
        self.traj = []
        self.trajectory = []
        self.brect = []
        self.alive = True
        self.ID = self._ID
        self.ghost = []
        for x in range(0,self.clip):  # this for loop initializes the bullets in the tank
            self.bxy.append(pygame.math.Vector2())
            self.bxy_prev.append(pygame.math.Vector2())
            self.dir.append(pygame.math.Vector2())
            self.tail.append(pygame.math.Vector2())
            self.traj.append(0)
            self.trajectory.append(0)
            self.active.append(False)
            self.firing.append(False)
            self.fuse.append(0)
            self.stun.append(0)


    def gun(self):  #function controls the Bullet logic
        for x in range(0, self.clip):
            if self.firing[x]: # This code is only ran when the tank has recently fired a bullet
                # finds the trajectory /D
                self.traj[x] = myslope(self.cent.x, self.cent.y, self.barrel.x, self.barrel.y)
                self.trajectory[x] = pygame.math.Vector2(self.traj[x])
                # converts to a unit vector /D
                self.dir[x] = (pygame.math.Vector2.normalize(self.trajectory[x])) * self.bullet_spd
                # places bullet at the end of the barrel /D
                self.bxy[x] = self.barrel + self.dir[x]

            if self.active[x]:  # this code only runs if the bullet is active and needs calculations done
                # moves bullet along the slope found earlier
                self.bxy[x] += self.dir[x] * 1.25
                self.stun[x] += 1
                # tail of the bullet /D
                self.tail[x] = self.bxy[x] - self.dir[x] * 5

                # if the bullet exists for more than 200 frames: delete the bullet /D
                if self.fuse[x] > self.fuse_val:
                    self.active[x] = False
                    self.fuse[x] = 0
                # firing stun prevents run and gunning /D
                if self.stun[x] > 1:
                    self.firing[x] = False
                    # bullet bounce /D
                if self.bxy[x].x > win_len:
                    self.dir[x].x = -self.dir[x].x
                    self.fuse[x] += 1
                if self.bxy[x].x < 0:
                    self.dir[x].x = -self.dir[x].x
                    self.fuse[x] += 1
                if self.bxy[x].y > win_ht:
                    self.dir[x].y = -self.dir[x].y
                    self.fuse[x] += 1
                if self.bxy[x].y < 0:
                    self.dir[x].y = -self.dir[x].y
                    self.fuse[x] += 1
                pygame.draw.line(WIN, self.bullet_c, self.tail[x], self.bxy[x], 4)
                self.bxy_prev[x] = self.bxy[x]

    def pc_control(self):  # This function allows the player to control the tank
        # saves the mouse coordinates as an xy vector
        # use this variable when doing anything with the mouse coordinates /D
        self.reticle = pygame.math.Vector2(pygame.mouse.get_pos())
        # calulates the exact center coordinates of the tank and stores as an xy vector /D
        self.cent = pygame.math.Vector2(self.x_coord + self.width * .5, self.y_coord + self.height * .5)
        # calculates the location of the endpoint of the barrel on the tank/D
        self.barrel = (pygame.math.Vector2.normalize((self.reticle - self.cent))) * self.barrel_len + self.cent
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:  # check if the quit button has been activated/D
                pygame.quit()
                sys.exit()
            # controls keyboard logic

            if keys[pygame.K_q]:  # hitting Q quits the game /D
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                for x in range(0, self.clip):
                    if ~self.active[x]:
                        # hitting Q quits the game /D
                        if self.active[x]:
                            continue
                        else:
                            self.active[x] = True
                            self.firing[x] = True
                            break
        # pc_tank controls for rectangle/D
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # up /D
            self.x_coord -= self.vel
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # down /D
            self.x_coord += self.vel
        if keys[pygame.K_w] or keys[pygame.K_UP]:  # left /D
            self.y_coord -= self.vel
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:  # right /D
            self.y_coord += self.vel
        # Boundry check /S
        if self.y_coord > win_ht - self.height:
            self.y_coord = win_ht - self.height
        if self.x_coord > win_len - self.width:
            self.x_coord = win_len - self.width
        if self.y_coord < 1:
            self.y_coord = 1
        if self.x_coord < 1:
            self.x_coord = 1



        # makes sure the pc_tank can not aim the reticle at their own tank /D
        if (self.reticle.x < self.barrel.x) & (self.reticle.x > self.cent.x):
            pygame.mouse.set_pos(self.barrel)
        if (self.reticle.x > self.barrel.x) & (self.reticle.x < self.cent.x):
            pygame.mouse.set_pos(self.barrel)
        # keep cursor in the bounds of the window
        # if (self.reticle.x >= win_len - 15):
        #     pygame.mouse.set_pos(win_len - 15, self.reticle.y)
        # if (self.reticle.x <= 15):
        #     pygame.mouse.set_pos(15, self.reticle.y)
        # if (self.reticle.y <= 15):
        #     pygame.mouse.set_pos(self.reticle.x, 15)
        # if (self.reticle.y >= win_ht - 5):
        #     pygame.mouse.set_pos(self.reticle.x, win_ht - 15)
        self.x_prev = self.x_coord
        pygame.draw.circle(WIN, self.reticle_c, (int(self.reticle.x), int(self.reticle.y)), 5, 1)

    def ai_control(self, tank_list): # function allows ai to control the tank
        close_tank = tank_list[0]
        for temp_tank in tank_list:
            # if  temp_tank.brain != self.brain: # checks for player tank
                if temp_tank == self:
                    continue

                if (abs(self.cent.x - temp_tank.cent.x)) < (abs(self.cent.x - close_tank.cent.x)) and abs(self.cent.y - temp_tank.cent.y) < (abs(self.cent.y - close_tank.cent.y)) :
                    close_tank = temp_tank #determines which tank is the closestwwwww


                self.reticle = pygame.math.Vector2(close_tank.cent) # aims at player
                    # # Pressure the player
                go = myslope(self.cent.x, self.cent.y, close_tank.cent.x, close_tank.cent.y)
                goo = pygame.math.Vector2(go[0], go[1])
                goo = pygame.math.Vector2.normalize(goo)
                if (abs(self.cent.x - close_tank.cent.x)) > 150:
                    self.x_coord += goo.x
                if (abs(self.cent.y - close_tank.cent.y)) > 150:
                    self.y_coord += goo.y
                eyesight = 250
                # Code for the AI to Avoid Bullets
                for x in range(0, temp_tank.clip):
                    if (abs(self.cent.x - temp_tank.bxy[x].x)) < eyesight:
                        if (abs(self.cent.y - temp_tank.bxy[x].y)) < eyesight:
                            perp = pygame.math.Vector2((0.001 + self.cent.x - temp_tank.bxy[x].x),
                                                       (0.001 + self.cent.y - temp_tank.bxy[x].y))
                            perp = pygame.math.Vector2.normalize(perp)
                            self.x_coord += perp.x
                            self.y_coord += perp.y
                for x in range(0, self.clip):
                    if (abs(self.cent.x - self.bxy[x].x)) < eyesight:
                        if (abs(self.cent.y - self.bxy[x].y)) < eyesight:
                            perp = pygame.math.Vector2((0.001 + self.cent.x - self.bxy[x].x),
                                                       (0.001 + self.cent.y - self.bxy[x].y))
                            perp = pygame.math.Vector2.normalize(perp)
                            self.x_coord += perp.x
                            self.y_coord += perp.y
                # saves the mouse coordinates as an xy vector
                # calulates the exact center coordinates of the tank and stores as an xy vector /D
                self.cent = pygame.math.Vector2(self.x_coord + self.width * .5, self.y_coord + self.height * .5)




                # Boundry check /S
                if self.y_coord > win_ht - self.height - 10:
                    self.y_coord = win_ht - self.height - 10
                if self.x_coord > win_len - self.width - 10:
                    self.x_coord = win_len - self.width - 10
                if self.y_coord < 10:
                    self.y_coord = 10
                if self.x_coord < 10:
                    self.x_coord = 10
                self.i += 1
                if self.i > self.timer:
                    self.reticle.x = (random.uniform(-100, 100)) + self.reticle.x
                    self.reticle.y = (random.uniform(-100, 100)) + self.reticle.y
                    self.i = 0
                    for x in range(0, self.clip):
                        if ~self.active[x]:
                            if self.active[x]:
                                continue
                            else:
                                self.active[x] = True
                                self.firing[x] = True

                                break
                # calculates the location of the endpoint of the barrel on the tank/D
                self.barrel = (pygame.math.Vector2.normalize((self.reticle - self.cent))) * self.barrel_len + self.cent

    # update display function
    def display(self):
        self.area = pygame.Rect(self.x_coord, self.y_coord, self.width, self.height)
        # tank barrel
        pygame.draw.line(WIN, self.barrel_c, self.cent, self.barrel, 5)
        # tank chasis
        pygame.draw.rect(WIN, self.body_c, self.area)
        # top of the pile

# Inheritance? check!
# upgraded stats for the tank

class smart(Tank_gen):
    def newcolor(self):

        if self.brain == TankBrain.PC:
            self.body_c = (150,10,220)
        if self.brain == TankBrain.COM:
            self.body_c = (100, 0, 100)

    def new_bullets(self):
        self.newcolor()
        if self.brain == TankBrain.PC:
            self.bullet_spd = 4
        else:
            self.bullet_spd = 1.5
        self.fuse_val = 4
        # Functionality to make bullets orbit the reticle

        for x in range(0,self.clip):
            if self.active[x]:
                # finds the trajectory /D
                dynam = myslope(self.bxy[x].x, self.bxy[x].y, self.reticle.x, self.reticle.y)
                self.dir[x] = (pygame.math.Vector2.normalize(dynam  + (self.dir[x]*1000)))*self.bullet_spd
                # places bullet at the end of the barrel /D
                self.bxy[x] += self.dir[x]
