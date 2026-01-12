from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import QTimer
from OpenGL.GL import *
from OpenGL.GLU import *

from .cube import CubeWidget
from .sphere import SphereWidget
from .shape import Shape


class ShapeWidget(QOpenGLWidget):
    def __init__(self, config):
        super().__init__()

        config_shape = config.model.shape
        self.current_shape = CubeWidget() if config_shape == "cube" else SphereWidget()
        config_color = {
            "r": config.model.shape_color_r,
            "g": config.model.shape_color_g,
            "b": config.model.shape_color_b,
        }
        self.color = (config_color["r"], config_color["g"], config_color["b"])
        self.angle = 0
        self.scale = 1

        # Update cube every 16ms (~60 FPS)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_angle)
        self.timer.start(16)

    def update_angle(self):
        self.angle += 1
        self.update()

    # ---- OpenGL setup ----
    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0, 0, 0, 0)  # transparent background

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, w / h, 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(0, 0, -5)
        glRotatef(self.angle, 1, 1, 0)
        glScale(self.scale, self.scale, self.scale)
        r, g, b = self.color
        glColor3f(r, g, b)

        self.current_shape.draw()

    def set_shape(self, shape_obj: Shape):
        self.current_shape = shape_obj
        self.update()

    def set_scale(self, value):
        self.scale = value
        self.update()
