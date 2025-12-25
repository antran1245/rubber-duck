from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget
from PySide6.QtCore import Qt, Signal


class OptionBox(QWidget):
    shapeSelected = Signal(str)
    randomColor = Signal()
    quitApplication = Signal()

    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)

        self.setAttribute(Qt.WA_TranslucentBackground)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setSpacing(1)
        label = QLabel("Shape Controls")
        label.setStyleSheet("color: white; font-size: 14px;")

        # Show Cube
        self.btn_cube = QPushButton("Show Cube")
        self.btn_cube.clicked.connect(lambda: self.shapeSelected.emit("cube"))
        # Show Sphere
        self.btn_sphere = QPushButton("Show Sphere")
        self.btn_sphere.clicked.connect(lambda: self.shapeSelected.emit("sphere"))
        # Random Color
        self.btn_random_color = QPushButton("Random Color")
        self.btn_random_color.clicked.connect(lambda: self.randomColor.emit())
        # Quit Application
        self.btn_quit_application = QPushButton("Quit Application")
        self.btn_quit_application.clicked.connect(lambda: self.quitApplication.emit())

        for btn in [
            self.btn_cube,
            self.btn_sphere,
            self.btn_random_color,
            self.btn_quit_application,
        ]:
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

        for element in [
            label,
            self.btn_cube,
            self.btn_sphere,
            self.btn_random_color,
            self.btn_quit_application,
        ]:
            layout.addWidget(element)
        self.setLayout(layout)

        self.resize(140, 100)
