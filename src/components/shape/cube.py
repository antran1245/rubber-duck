from OpenGL.GL import *
from OpenGL.GLU import *

from .shape import Shape


class CubeWidget(Shape):
    # ---- cube ----
    def draw(self):
        glBegin(GL_QUADS)

        glVertex3f(1, 1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, 1, 1)
        glVertex3f(1, 1, 1)

        glVertex3f(1, -1, 1)
        glVertex3f(-1, -1, 1)
        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)

        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)

        glVertex3f(1, -1, -1)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(1, 1, -1)

        glVertex3f(-1, 1, 1)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, -1, 1)

        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, -1, -1)

        glEnd()
