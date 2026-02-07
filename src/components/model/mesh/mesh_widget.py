from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import QTimer

from OpenGL.GL import *
from OpenGL.GLU import *


class MeshWidget(QOpenGLWidget):

    def __init__(self):
        super().__init__()

        self.model = None
        self.rotation = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)

    def setModel(self, model):
        self.model = model
        self.update()

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.12, 0.12, 0.12, 1)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, w / max(h, 1), 0.1, 100)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(0, 2, 6, 0, 0, 0, 0, 1, 0)
        glRotate(self.rotation, 0, 1, 0)
        if self.model:
            self.model.draw()

    def animate(self):
        self.rotation += 0.4
        self.update()
