from OpenGL.GL import *
from OpenGL.GLU import *

from .shape import Shape


class SphereWidget(Shape):
    def __init__(self):
        super().__init__()

        # Sphere setting
        self.sphere_radius = 1.4
        self.sphere_vertical_segments = 8
        self.sphere_horizontal_segments = 8
        self.sphere_edge_width = 1

    def draw(self):
        self.draw_solid()
        self.draw_edges()

    def draw_solid(self):
        quadric = gluNewQuadric()
        gluSphere(
            quadric,
            self.sphere_radius,
            self.sphere_vertical_segments,
            self.sphere_horizontal_segments,
        )
        gluDeleteQuadric(quadric)

    def draw_edges(self):
        glColor3f(0, 0, 0)
        glLineWidth(self.sphere_edge_width)

        quadric = gluNewQuadric()
        gluQuadricDrawStyle(quadric, GLU_LINE)
        gluSphere(
            quadric,
            self.sphere_radius,
            self.sphere_vertical_segments,
            self.sphere_horizontal_segments,
        )
        gluDeleteQuadric(quadric)
