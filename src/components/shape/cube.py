from OpenGL.GL import *
from OpenGL.GLU import *

from .shape import Shape


class CubeWidget(Shape):
    # ---- cube ----
    def draw(self):
        glBegin(GL_QUADS)

        glColor3f(1, 0, 0)  # Red
        glVertex3f(1, 1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, 1, 1)
        glVertex3f(1, 1, 1)

        glColor3f(0, 1, 0)  # Green
        glVertex3f(1, -1, 1)
        glVertex3f(-1, -1, 1)
        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)

        glColor3f(0, 0, 1)  # Blue
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)

        glColor3f(1, 1, 0)  # Yellow
        glVertex3f(1, -1, -1)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(1, 1, -1)

        glColor3f(1, 0, 1)  # Purple
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, -1, 1)

        glColor3f(0, 1, 1)  # Cyan
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, -1, -1)

        glEnd()
