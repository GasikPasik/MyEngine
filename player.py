from pygame import K_s, K_w, K_a, K_d, K_SPACE, K_LCTRL, K_LSHIFT
from math import sin, cos, radians

class Player:

    def __init__(self, x=0, y=0, z=0, angle=180, **kwargs):
        self.x = x
        self.y = y
        self.z = z

        self.rx = 90 + angle
        self.ry = 0

        self.angle = angle

        self.speed = 0.01
        self.boost = 0
        self.speed_of_boost = 0.01
        self.max_x_boost = 5
        
        self.speed_rotate_x = 0.025
        self.speed_rotate_y = 0.018

        self.dir = {K_w : 0, K_s: 0, K_a: 0, K_d: 0, K_SPACE: 0, K_LCTRL: 0}

    def move(self):

        if(self.boost != 0):
            if(self.boost < self.max_x_boost):
                self.boost += self.speed_of_boost

        cur_speed = round(self.speed + self.speed*self.boost, 4)

        k_y = round(1*sin(radians(self.angle)), 4)
        k_x = round(1*cos(radians(self.angle)), 4)

        # FORWARD | BACK
        if(self.dir[K_w] == 2):
            self.x += cur_speed * k_x
        elif(self.dir[K_s] == 2):
            self.x -= cur_speed * k_x
        elif(self.dir[K_w] == 1):
            self.x += cur_speed * k_x
        elif(self.dir[K_s] == 1):
            self.x -= cur_speed * k_x

        if(self.dir[K_w] > 0):
            self.y += cur_speed * k_y

        if(self.dir[K_s] > 0):
            self.y -= cur_speed * k_y

        # LEFT | RIGHT
        x_left= round(k_x * cos(radians(90)) - k_y * sin(radians(90)), 4)
        y_left = round(k_x * sin(radians(90)) + k_y * cos(radians(90)), 4)
        x_right = round(k_x * cos(radians(-90)) - k_y * sin(radians(-90)), 4)
        y_right = round(k_x * sin(radians(-90)) + k_y * cos(radians(-90)), 4)
        
        if(self.dir[K_d] == 2):
            self.x += cur_speed * x_right
        elif(self.dir[K_a] == 2):
            self.x += cur_speed * x_left
        elif(self.dir[K_d] == 1):
            self.x += cur_speed * x_right
        elif(self.dir[K_a] == 1):
            self.x += cur_speed * x_left

        if(self.dir[K_a] > 0):
            self.y += cur_speed * y_left
        
        if(self.dir[K_d] > 0):
            self.y += cur_speed * y_right

        # UP | UNDER
        if(self.dir[K_SPACE] == 2):
            self.z += cur_speed
        elif(self.dir[K_LCTRL] == 2):
            self.z -= cur_speed
        elif(self.dir[K_SPACE] == 1):
            self.z += cur_speed
        elif(self.dir[K_LCTRL] == 1):
            self.z -= cur_speed



        self.x = round(self.x, 4)
        self.y = round(self.y, 4)
        self.z = round(self.z, 4)
        
    def handleRotateCamera(self, new_rotate):
        self.rx = round(self.rx + self.speed_rotate_x*new_rotate[0], 5)
        self.ry = round(self.ry + self.speed_rotate_y*new_rotate[1], 5)

        self.angle = round(( self.angle + self.rx ) % 360, 3)

    def handleMove(self, key, is_press):

        if(key == K_LSHIFT):
            if(is_press):
                self.boost = 0.01
            else:
                self.boost = 0
            return
            
        if(not is_press):
            self.dir[key] = 0
            return
        

        if(key == K_w):
            if(self.dir[K_s] > 0):
                self.dir[K_w] = 2
                self.dir[K_s] = 1
            else:
                self.dir[K_w] = 1
        
        elif(key == K_s):
            if(self.dir[K_w] > 0):
                self.dir[K_s] = 2
                self.dir[K_w] = 1
            else:
                self.dir[K_s] = 1
        
        elif(key == K_a):
            if(self.dir[K_d] > 0):
                self.dir[K_a] = 2
                self.dir[K_d] = 1
            else:
                self.dir[K_a] = 1

        elif(key == K_d):
            if(self.dir[K_a] > 0):
                self.dir[K_d] = 2
                self.dir[K_a] = 1
            else:
                self.dir[K_d] = 1

        elif(key == K_SPACE):
            if(self.dir[K_LCTRL] > 0):
                self.dir[K_SPACE] = 2
                self.dir[K_LCTRL] = 1
            else:
                self.dir[K_SPACE] = 1

        elif(key == K_LCTRL):
            if(self.dir[K_SPACE] > 0):
                self.dir[K_LCTRL] = 2
                self.dir[K_SPACE] = 1
            else:
                self.dir[K_LCTRL] = 1

    
               
    def update(self):
       
       self.move()






