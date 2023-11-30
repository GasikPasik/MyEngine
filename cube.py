from OpenGL.GL import glColor3f, glBegin, glEnd, glVertex3f, glTranslatef, GL_POLYGON
class Cube():

    def __init__(self, size, x=0, y=0, z=0, color=(255, 255, 255)):

        self.x = x
        self.y = y
        self.z = z
        
        self.size = size
        self.h_size = size/2

        self.boost_of_fall = 0.01
        self.speed_of_fall = 0.02

        self.vertices = [(self.h_size, self.h_size, -self.h_size),
                        (self.h_size, -self.h_size, -self.h_size),
                        (-self.h_size, -self.h_size, -self.h_size),
                        (-self.h_size, self.h_size, -self.h_size),
                        (self.h_size, self.h_size, self.h_size), # 4
                        (self.h_size, -self.h_size, self.h_size),
                        (-self.h_size, -self.h_size, self.h_size),
                        (-self.h_size, self.h_size, self.h_size)]
    def getVertex(self, number):
        corner = self.vertices[number]
        corner[0] += self.x
        corner[1] += self.y 
        corner[2] += self.z

        return corner

    def isCubeUnder(self, cube):
        
        if(self.z - self.h_size > cube.z + cube.h_size):
            return False
        
        if(self.z + self.h_size < cube.z - cube.h_size): 
            return False
        

        if(self.y - self.h_size > cube.y + cube.h_size):
            return False
        
        if(self.y + self.h_size < cube.y - cube.h_size): 
            return False
        
        
        if(self.x - self.h_size > cube.x + cube.h_size):
            return False
        
        if(self.x + self.h_size < cube.x - cube.h_size): 
            return False
        

        if(cube.z > self.z):
            self.z += self.speed_of_fall
        
        return True
        
    
    def underCollision(self, ALL_CUBES):
        
        for cube in ALL_CUBES:
            if(self.isCubeUnder(cube)):
                return True
        
        return False
    
    def move(self, ALL_CUBES):
        if(self.z <= 0 + self.h_size):
            self.z = self.h_size
            return
        
        if(not self.underCollision(ALL_CUBES)):
            self.z -= self.speed_of_fall

    def draw(self):

        glTranslatef(self.x, self.y, self.z)

        for i in range(4):
            glColor3f(0.2*i, 0.5, 1)
          
            glBegin(GL_POLYGON)
                    
            glVertex3f(*self.vertices[i])
            glVertex3f(*self.vertices[(i + 1) % 4])
            glVertex3f(*self.vertices[((i + 5) % 4) + 4])
            glVertex3f(*self.vertices[i + 4])

            glEnd()

        for i in [0, 4]:
            glColor3f(0.4, 0.5, 0.2*i)
          
            glBegin(GL_POLYGON)
                    
            glVertex3f(*self.vertices[i])
            glVertex3f(*self.vertices[i+1])
            glVertex3f(*self.vertices[i+2])
            glVertex3f(*self.vertices[i+3])

            glEnd()

        glTranslatef(-self.x, -self.y, -self.z)

        
    