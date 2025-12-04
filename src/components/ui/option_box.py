from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QPushButton,
)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import Qt, Signal


class OptionBox(QOpenGLWidget):
    shapeSelected = Signal(str)

    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)

        self.setAttribute(Qt.WA_TranslucentBackground)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        label = QLabel("Shape Controls")
        label.setStyleSheet("color: white; font-size: 14px;")

        self.btn_cube = QPushButton("Show Cube")
        self.btn_cube.clicked.connect(lambda: self.shapeSelected.emit("cube"))

        self.btn_sphere = QPushButton("Show Sphere")
        self.btn_sphere.clicked.connect(lambda: self.shapeSelected.emit("sphere"))

        for btn in [self.btn_cube, self.btn_sphere]:
            btn.setStyleSheet(
                """
              QPushButton {
                  background: rgba(30,30,30,180);
                  color: white;
                  padding: 6px;
                  border-radius: 8px;
              }
              QPushButton:hover {
                  background: rgba(60,60,60,200);
              }
          """
            )

        layout.addWidget(label)
        layout.addWidget(self.btn_cube)
        layout.addWidget(self.btn_sphere)
        self.setLayout(layout)

        self.resize(140, 100)
