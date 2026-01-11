from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal

from src.config import set_shape
from .layout_base import LayoutBase
from .option_controller import ShapeController


class ModelsOption(LayoutBase):
    modelsColorOption = Signal()

    def __init__(self, shape_widget: QOpenGLWidget):
        # Declare classes
        self.shape_controller = ShapeController(shape_widget)

        # Show Cube
        self.btn_cube = QPushButton("Show Cube")
        self.btn_cube.clicked.connect(lambda: self.handle_shape_controller("cube"))
        # Show Sphere
        self.btn_sphere = QPushButton("Show Sphere")
        self.btn_sphere.clicked.connect(lambda: self.handle_shape_controller("sphere"))

        # Select Color
        self.btn_color = QPushButton("Color")
        self.btn_color.clicked.connect(lambda: self.modelsColorOption.emit())

        title = "Select a Model"
        buttons_list = [self.btn_cube, self.btn_sphere, self.btn_color]
        super().__init__(title=title, buttons_list=buttons_list)

    ### Handle shape controller
    def handle_shape_controller(self, value=""):
        self.shape_controller.switch_shape(value)
        set_shape(value)
