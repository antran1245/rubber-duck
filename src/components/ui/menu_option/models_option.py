from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal

from src.config import set_shape
from .layout_base import LayoutBase
from src.components.model.shape import CubeWidget, SphereWidget


class ModelsOption(LayoutBase):
    modelsColorOption = Signal()

    def __init__(self, shape_widget: QOpenGLWidget):
        self.shape_widget = shape_widget

        self.shapes = {"cube": CubeWidget(), "sphere": SphereWidget()}

        # Show Cube
        self.btn_cube = QPushButton("Show Cube")
        self.btn_cube.clicked.connect(lambda: self.handle_shape_controller("cube"))
        # Show Sphere
        self.btn_sphere = QPushButton("Show Sphere")
        self.btn_sphere.clicked.connect(lambda: self.handle_shape_controller("sphere"))
        # Use Model
        self.btn_model = QPushButton("Upload 3D Model")
        self.btn_model.clicked.connect(lambda: print("Use Model"))
        # Select Color
        self.btn_color = QPushButton("Color")
        self.btn_color.clicked.connect(lambda: self.modelsColorOption.emit())

        title = "Select a Model"
        buttons_list = [self.btn_cube, self.btn_sphere, self.btn_color]
        super().__init__(title=title, buttons_list=buttons_list)

    def switch_shape(self, selected_shape):
        if selected_shape in self.shapes:
            self.shape_widget.set_shape(self.shapes[selected_shape])
            return f"Switched to: {selected_shape}"
        else:
            return f"{selected_shape.capitalize()} does not exist."

    ### Handle shape controller
    def handle_shape_controller(self, value=""):
        self.switch_shape(value)
        set_shape(value)
