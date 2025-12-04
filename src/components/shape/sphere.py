from OpenGL.GL import *
from OpenGL.GLU import *

from .shape import Shape


class SphereWidget(Shape):
    def draw(self):
        glColor3f(0.8, 0.4, 0.2)
        quadric = gluNewQuadric()
        gluSphere(quadric, 1.4, 32, 32)
        gluDeleteQuadric(quadric)
