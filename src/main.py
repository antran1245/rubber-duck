# main.py
import sys
import math
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QSurfaceFormat
from PySide6.QtOpenGLWidgets import QOpenGLWidget

# Use PyOpenGL for GL calls
from OpenGL.GL import *
from OpenGL.GLU import *


class GLCubeWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.angle = 0.0
        self.setAttribute(Qt.WA_TranslucentBackground)  # allow transparent background
        self.setAutoFillBackground(False)

        # Timer for animation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start(16)  # ~60 FPS

    def on_timeout(self):
        self.angle += 0.6
        if self.angle >= 360.0:
            self.angle -= 360.0
        self.update()

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glClearColor(0.0, 0.0, 0.0, 0.0)  # fully transparent background

    def resizeGL(self, w, h):
        if h == 0:
            h = 1
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect = w / h
        gluPerspective(45.0, aspect, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # camera
        gluLookAt(0, 0, 6,   # eye
                  0, 0, 0,   # center
                  0, 1, 0)   # up

        # rotate cube
        glRotatef(self.angle, 1.0, 1.0, 0.0)

        # Draw cube (semi-opaque so transparency shows)
        self.draw_colored_cube()

    def draw_colored_cube(self):
        # Each face a different color with alpha
        glBegin(GL_QUADS)
        # Front (z+)
        glColor4f(1, 0, 0, 0.9)
        glVertex3f(-1, -1,  1)
        glVertex3f( 1, -1,  1)
        glVertex3f( 1,  1,  1)
        glVertex3f(-1,  1,  1)
        # Back (z-)
        glColor4f(0, 1, 0, 0.9)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1,  1, -1)
        glVertex3f( 1,  1, -1)
        glVertex3f( 1, -1, -1)
        # Left (x-)
        glColor4f(0, 0, 1, 0.9)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, -1,  1)
        glVertex3f(-1,  1,  1)
        glVertex3f(-1,  1, -1)
        # Right (x+)
        glColor4f(1, 1, 0, 0.9)
        glVertex3f(1, -1, -1)
        glVertex3f(1,  1, -1)
        glVertex3f(1,  1,  1)
        glVertex3f(1, -1,  1)
        # Top (y+)
        glColor4f(1, 0, 1, 0.9)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, 1,  1)
        glVertex3f( 1, 1,  1)
        glVertex3f( 1, 1, -1)
        # Bottom (y-)
        glColor4f(0, 1, 1, 0.9)
        glVertex3f(-1, -1, -1)
        glVertex3f( 1, -1, -1)
        glVertex3f( 1, -1,  1)
        glVertex3f(-1, -1,  1)
        glEnd()


class FloatingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Floating 3D Pet")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.Tool)  # usually hides from taskbar

        # If you want click-through behavior (mouse passes through),
        # enable the following flag. WARNING: makes the window non-interactive.
        # self.setWindowFlag(Qt.WindowTransparentForInput)

        # central OpenGL widget
        self.gl_widget = GLCubeWidget(self)
        self.setCentralWidget(self.gl_widget)

        # default size & position
        self.resize(320, 320)
        # optional: move to bottom-right-ish
        screen = QApplication.primaryScreen().availableGeometry()
        self.move(screen.width() - 360, screen.height() - 400)


def main():
    # Request a surface format that is compatible
    fmt = QSurfaceFormat()
    fmt.setDepthBufferSize(24)
    QSurfaceFormat.setDefaultFormat(fmt)

    app = QApplication(sys.argv)

    w = FloatingWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
