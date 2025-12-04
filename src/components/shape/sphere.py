from OpenGL.GL import *
from OpenGL.GLU import *

from .shape import Shape


class SphereWidget(Shape):
    def draw(self):
        quadric = gluNewQuadric()
        gluSphere(quadric, 1.4, 32, 32)
        gluDeleteQuadric(quadric)
