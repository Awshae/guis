import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import sys

def draw_cylinder(radius, height, num_slices):
    r = radius
    h = height
    n = float(num_slices)

    

    circle_pts = []
    for i in range(int(n) + 1):
        angle = 2 * math.pi * (i/n)
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        pt = (x, y)
        circle_pts.append(pt)

    glBegin(GL_TRIANGLE_FAN)#drawing the back circle
    glColor(1, 0, 0)
    glVertex(0, 0, h/2.0)
    for (x, y) in circle_pts:
        z = h/2.0
        glColor(0, 0, 1)
        glVertex(x, y, z)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)#drawing the front circle
    glColor(1, 0, 0)
    glVertex(0, 0, -h/2.0)
    for (x, y) in circle_pts:
        z = -h/2.0
        glColor(0, 0, 1)
        glVertex(x, y, z)
    glEnd()

    glBegin(GL_TRIANGLE_STRIP)#draw the tube
    for (x, y) in circle_pts:
        z = h/2.0
        glVertex(x, y, z)
        glColor(0, 1, 0)
        glVertex(x, y, -z)
        glColor(1,1,0)
    glEnd()

pygame.init()
(width, height) = (1366, 786)
screen = pygame.display.set_mode((width, height), OPENGL | DOUBLEBUF)
clock = pygame.time.Clock()
rotation_x = 0.0
rotation_y = 0.0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        rotation_x += 1.0
        glRotate(1.0, 1.0, 0.0, 0.0)

    if keys[pygame.K_DOWN]:
        rotation_x -= 1.0
        glRotate(-1.0, 1.0, 0.0, 0.0)

    if keys[pygame.K_RIGHT]:
        rotation_y += 1.0
        glRotate(1.0, 0.0, 1.0, 0.0)

    if keys[pygame.K_LEFT]:
        rotation_y -= 1.0
        glRotate(-1.0, 0.0, 1.0, 0.0)

    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30, float(width)/height, 1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(0, 0, -50)
    glRotate(rotation_x,1, 0, 0)
    glRotate(rotation_y,0, 1, 0)

    draw_cylinder(4, 7, 1000)
    pygame.display.flip()
    clock.tick(60)
