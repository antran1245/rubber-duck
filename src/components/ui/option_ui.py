from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal
from .layout_base import LayoutBase


class OptionUI(LayoutBase):
    shapeSelected = Signal(str)
    randomColor = Signal()
    quitApplication = Signal()

    def __init__(self):

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

        title = "Shape Controls"
        buttons_list = [
            self.btn_cube,
            self.btn_sphere,
            self.btn_random_color,
            self.btn_quit_application,
        ]
        super().__init__(title=title, buttons_list=buttons_list)
