from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import QPushButton
from .layout_base import LayoutBase

from .option_controller import ShapeController
from .models_color_option import ModelsColorOption


class ModelsOption(LayoutBase):

    def __init__(self, shape_widget: QOpenGLWidget):
        # Declare classes
        self.shape_controller = ShapeController(shape_widget)
        self.models_color_option = ModelsColorOption()

        # Show Cube
        self.btn_cube = QPushButton("Show Cube")
        self.btn_cube.clicked.connect(
            lambda: self.handle_shape_controller("switch_shape", "cube")
        )
        # Show Sphere
        self.btn_sphere = QPushButton("Show Sphere")
        self.btn_sphere.clicked.connect(
            lambda: self.handle_shape_controller("switch_shape", "sphere")
        )

        # Random Color
        self.btn_random_color = QPushButton("Random Color")
        self.btn_random_color.clicked.connect(
            lambda: self.handle_shape_controller("random_color")
        )

        title = "Select a Model"
        buttons_list = [self.btn_cube, self.btn_sphere, self.btn_random_color]
        super().__init__(title=title, buttons_list=buttons_list)

    ### Handle shape controller
    def handle_shape_controller(self, action, value=""):
        if action == "switch_shape":
            self.shape_controller.switch_shape(value)
        elif action == "random_color":
            new_color_value = self.shape_controller.random_color()
            self.models_color_option.update_color_values(new_color_value)
