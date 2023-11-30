import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from grid import Grid
from player import Player
from cube import Cube

from random import uniform

WINDOW_SIZE = (600, 600)
focus_mouse = False

grid = Grid(size=8)
player = Player(5, -5, 1, 180)

ALL_CUBES = []
ALL_CUBES.append(Cube(0.2, 0.5, 0.5, 2))
ALL_CUBES.append(Cube(0.15, 0, 0.5, 4))
ALL_CUBES.append(Cube(0.4, 0, -1.3, 2))
ALL_CUBES.append(Cube(0.2, 0, -1.1, 3))

viewMatrix = None

def keyDownHandle(key):
    match key:

        case pg.K_F2: 
            global focus_mouse
            focus_mouse = not focus_mouse
           # print(f"Focus mouse: { focus_mouse}")

            pg.mouse.set_visible(not focus_mouse)
            pg.event.set_grab(focus_mouse)

    
        case pg.K_F4: 
            print("\nDEBUG INFO:")
            print("\n\tPlayer")
            print(f"\tx:{player.x} y:{player.y} z:{player.z}")
            print(f"\trx:{player.rx} ry:{player.ry}")
            print(f"\tdir: {player.dir}")
            print(f"\tangle: {player.angle}")
            print(f"\tcurSpeed: {round((player.speed + player.speed * player.boost) * 100, 3)}")

            print(f'\n\t{focus_mouse=}')


            print()

        case pg.K_F6:
            ALL_CUBES.append(Cube(uniform(0,1), uniform(-5,5), uniform(-5,5), uniform(2, 6))) 

        case pg.K_a | pg.K_d | pg.K_w | pg.K_s | pg.K_SPACE | pg.K_LCTRL | pg.K_LSHIFT:
            player.handleMove(key, 1)

def keyUpHandle(key):
    match key:
        case pg.K_a | pg.K_d | pg.K_w | pg.K_s | pg.K_SPACE | pg.K_LCTRL | pg.K_LSHIFT:
            player.handleMove(key, 0)

def draw(screen):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    for cube in ALL_CUBES:
        cube.draw()

    grid.draw()

def fixedUpdate():
    for idx, cube in enumerate(ALL_CUBES):
        cube.move(ALL_CUBES[:idx] + ALL_CUBES[idx+1:])

def handleRotateOfPlayer(screen):
    if(not focus_mouse):
        return
    
    new_rotate = pg.mouse.get_pos()
    new_rotate = [WINDOW_SIZE[i]/2 - new_rotate[i] for i in range(2)]
    
    player.handleRotateCamera(new_rotate)

    pg.mouse.set_pos(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2)

rotate_z = 180

def update(screen):
    while True:
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    pg.quit()
                    return
                
                case pg.KEYDOWN:
                    keyDownHandle(event.key)
                
                case pg.KEYUP:
                    keyUpHandle(event.key)
        

        handleRotateOfPlayer(screen)
        player.update()

        glLoadIdentity()
        gluPerspective(60, (WINDOW_SIZE[0]/WINDOW_SIZE[1]), 0.1, 50.0)

        glRotatef(-player.ry, 1.0, 0.0, 0.0)
        
        glPushMatrix()
        glLoadIdentity()

        glRotatef(-player.rx, 0.0, 1.0, 0.0)
        player.rx = 0
        global viewMatrix
        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        glPopMatrix()
        glMultMatrixf(viewMatrix)

        glTranslatef(player.x, player.y, -player.z)
        
        fixedUpdate()
        draw(screen)


        pg.display.flip()
        pg.time.wait(10)
    


def main():
    print("Start game..")

    pg.init()
    screen = pg.display.set_mode(WINDOW_SIZE, DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)

    global viewMatrix
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, -5, 0, 0, 0, 0, 0, 0, 1)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)


    update(screen)

    print("Exit..")


if __name__ == "__main__":
    main()