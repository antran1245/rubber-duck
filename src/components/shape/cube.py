from OpenGL.GL import *
from OpenGL.GLU import *

from .shape import Shape


class CubeWidget(Shape):
    # ---- cube ----
    def __init__(self):
        super().__init__()

        # Cube setting
        self.cube_edge_width = 2

    def draw(self):
        self.draw_solid()
        self.draw_edges()

    def draw_solid(self):
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

    def draw_edges(self):
        glColor3f(0, 0, 0)
        glLineWidth(self.cube_edge_width)

        glBegin(GL_LINES)

        edges = [
            # front square
            (-1, -1, 1),
            (1, -1, 1),
            (1, -1, 1),
            (1, 1, 1),
            (1, 1, 1),
            (-1, 1, 1),
            (-1, 1, 1),
            (-1, -1, 1),
            # back square
            (-1, -1, -1),
            (1, -1, -1),
            (1, -1, -1),
            (1, 1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            # connecting lines
            (-1, -1, 1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, -1, -1),
            (1, 1, 1),
            (1, 1, -1),
            (-1, 1, 1),
            (-1, 1, -1),
        ]

        for v in edges:
            glVertex3f(*v)

        glEnd()
