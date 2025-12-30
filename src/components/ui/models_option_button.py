from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal
from .layout_base import LayoutBase


class ModelsOptionButton(LayoutBase):
    shapeSelected = Signal(str)

    def __init__(self):
        # Show Cube
        self.btn_cube = QPushButton("Show Cube")
        self.btn_cube.clicked.connect(lambda: self.shapeSelected.emit("cube"))
        # Show Sphere
        self.btn_sphere = QPushButton("Show Sphere")
        self.btn_sphere.clicked.connect(lambda: self.shapeSelected.emit("sphere"))

        title = "Select a Model"
        buttons_list = [
            self.btn_cube,
            self.btn_sphere,
        ]
        super().__init__(title=title, buttons_list=buttons_list)
