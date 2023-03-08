import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def draw_pyramid():
    glBegin(GL_TRIANGLES)
    # Front face
    glColor3f(0.1,1.0,1.0)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    # Right face
    glColor3f(0.38,0.78,0.79)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)

    # Back face
    glColor3f(0.2,0.6,0.6)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)

    # Left face
    glColor3f(0.05, 0.7, 0.7)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.09, 0.39, 0.5)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
         # Get the list of keys pressed
        keys = pygame.key.get_pressed()

        # Check if the arrow keys are pressed and modify rotation accordingly
        if keys[pygame.K_LEFT]:
            glRotate(1, 0, 1, 0)
        if keys[pygame.K_RIGHT]:
            glRotate(1, 0, -1, 0)
        if keys[pygame.K_UP]:
            glRotate(1, 1, 0, 0)
        if keys[pygame.K_DOWN]:
            glRotate(1, -1, 0, 0)

        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_pyramid()
        pygame.display.flip()
        pygame.time.wait(10)

main()
