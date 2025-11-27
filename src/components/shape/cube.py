from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import QTimer
from OpenGL.GL import *
from OpenGL.GLU import *


class CubeWidget(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.angle = 0

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

        self.draw_cube()

    # ---- cube ----
    def draw_cube(self):
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
