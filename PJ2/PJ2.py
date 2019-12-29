from OpenGL.GL import *

from OpenGL.GLU import *
from OpenGL.GLUT import *


def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(0.1, 0, 1, 0)
    glutWireTeapot(0.5)
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowPosition(0, 0)
glutInitWindowSize(800, 800)
glutCreateWindow(b"Teapot")
glutDisplayFunc(drawFunc)
glutIdleFunc(drawFunc)
glutMainLoop()
