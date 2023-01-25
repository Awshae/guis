from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import pygame
from pygame.locals import *

def renderPyramid(base, height):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    x = base/2

    glColor3f(1.0, 0.0, 0.0)  # red
    glVertex3f(0.0, height, 0.0)  # top
    glColor3f(0.0, 1.0, 0.0)  # green
    glVertex3f(-x, -x, x)  # front-left
    glColor3f(0.0, 0.0, 1.0)  # blue
    glVertex3f(x, -x, x)  # front-right

    glColor3f(1.0, 0.0, 0.0)  # red
    glVertex3f(0.0, height, 0.0)  # top
    glColor3f(0.0, 0.0, 1.0)  # blue
    glVertex3f(x, -x, x)  # front-right
    glColor3f(0.0, 1.0, 0.0)  # green
    glVertex3f(x, -x, -x)  # back-right

    glColor3f(1.0, 0.0, 0.0)  # red
    glVertex3f(0.0, height, 0.0)  # top
    glColor3f(0.0, 1.0, 0.0)  # green
    glVertex3f(x, -x, -x)  # back-right
    glColor3f(0.0, 0.0, 1.0)  # blue
    glVertex3f(-x, -x, -x)  # back-left

    glColor3f(1.0, 0.0, 0.0)  # red
    glVertex3f(0.0, height, 0.0)  # top
    glColor3f(0.0, 0.0, 1.0)  # blue
    glVertex3f(-x, -x, -x)  # back-left
    glColor3f(0.0, 1.0, 0.0)  # green
    glVertex3f(-x, -x, x)  # front-left

    glEnd()
    glFlush()


pygame.init()
(width, height) = (1366, 786)
screen = pygame.display.set_mode((width, height), OPENGL | DOUBLEBUF)
clock = pygame.time.Clock()
rotation = 0.0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rotation += 1.0
    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30, float(width)/height, 1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(0, 0, -50)
    glRotate(rotation, 1, 1, 1)

    renderPyramid(10,5)
    pygame.display.flip()
    clock.tick(60)


