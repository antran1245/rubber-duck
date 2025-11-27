from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QPushButton,
)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import Qt


class OptionBox(QOpenGLWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)

        self.setAttribute(Qt.WA_TranslucentBackground)

        layout = QVBoxLayout()
        label = QLabel("Shape Controls")
        label.setStyleSheet("color: white; font-size: 14px;")

        btn_cube = QPushButton("Show Cube")

        for btn in [btn_cube]:
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
        layout.addWidget(btn_cube)
        self.setLayout(layout)

        self.resize(140, 100)
