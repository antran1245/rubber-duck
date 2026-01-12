from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import QPushButton, QSlider, QLabel
from PySide6.QtCore import Qt

from src.config import get_shape_color, set_shape_color
from .option_controller import ShapeController
from .layout_base import LayoutBase


class ModelsColorOption(LayoutBase):

    def __init__(self, shape_widget: QOpenGLWidget):
        # Declare classes
        self.shape_controller = ShapeController(shape_widget)

        color = get_shape_color()
        self.red = color["r"] or 1.0
        self.green = color["g"] or 1.0
        self.blue = color["b"] or 1.0

        # Random Color
        self.btn_random_color = QPushButton("Random Color")
        self.btn_random_color.clicked.connect(lambda: self.handle_shape_controller())

        title = "Select a Color"
        buttons_list = [self.btn_random_color]
        super().__init__(title=title, buttons_list=buttons_list)

        # Slider for RGB
        slider_red_label = QLabel("Red")
        self.slider_red = QSlider(Qt.Orientation.Horizontal)
        self.slider_red.valueChanged.connect(
            lambda value: self.value_changed(value, "red")
        )

        slider_green_label = QLabel("Green")
        self.slider_green = QSlider(Qt.Orientation.Horizontal)
        self.slider_green.valueChanged.connect(
            lambda value: self.value_changed(value, "green")
        )

        slider_blue_label = QLabel("Blue")
        self.slider_blue = QSlider(Qt.Orientation.Horizontal)
        self.slider_blue.valueChanged.connect(
            lambda value: self.value_changed(value, "blue")
        )

        ### Style and Adding to the layout
        for slider in [self.slider_red, self.slider_green, self.slider_blue]:
            slider.setRange(0, 255)
            slider.sliderReleased.connect(self.slider_released)

        self.slider_red.setValue(color["r"] * 255)
        self.slider_green.setValue(color["g"] * 255)
        self.slider_blue.setValue(color["b"] * 255)

        for label in [slider_red_label, slider_green_label, slider_blue_label]:
            label.setStyleSheet(
                """
                    QLabel {
                        color: white;
                    }
                """
            )

        for ele in [
            slider_red_label,
            self.slider_red,
            slider_green_label,
            self.slider_green,
            slider_blue_label,
            self.slider_blue,
        ]:
            self.layout.addWidget(ele)

    ### Slider update
    def value_changed(self, value, color):
        self.red = value / 255 if color == "red" else self.red
        self.green = value / 255 if color == "green" else self.green
        self.blue = value / 255 if color == "blue" else self.blue
        self.update_color_values()

    def slider_released(self):
        set_shape_color(self.red, self.green, self.blue)

    ### Update the shape color
    def update_color_values(self):
        self.shape_controller.update_color(self.red, self.green, self.blue)

    ### Handle shape controller
    def handle_shape_controller(self):
        new_color_value = self.shape_controller.random_color()
        self.red = new_color_value["red"]
        self.green = new_color_value["green"]
        self.blue = new_color_value["blue"]
        set_shape_color(self.red, self.green, self.blue)
        self.slider_red.setValue(self.red * 255)
        self.slider_green.setValue(self.green * 255)
        self.slider_blue.setValue(self.blue * 255)
