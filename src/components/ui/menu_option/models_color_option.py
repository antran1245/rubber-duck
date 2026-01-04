from PySide6.QtWidgets import QPushButton, QSlider, QLabel
from PySide6.QtCore import Qt, Signal
from .layout_base import LayoutBase


class ModelsColorOption(LayoutBase):
    randomColor = Signal()
    updateColor = Signal(int, int, int)

    def __init__(self):

        self.red = 0
        self.green = 0
        self.blue = 0

        # Random Color
        self.btn_random_color = QPushButton("Random Color")
        self.btn_random_color.clicked.connect(lambda: self.randomColor.emit())

        title = "Select a Color"
        buttons_list = [self.btn_random_color]
        super().__init__(title=title, buttons_list=buttons_list)

        # Slider for RGB
        slider_red_label = QLabel("Red")
        self.slider_red = QSlider(Qt.Orientation.Horizontal)
        self.slider_red.setRange(0, 255)
        self.slider_red.setSingleStep(1)
        self.slider_red.valueChanged.connect(self.value_changed, "red")

        slider_green_label = QLabel("Green")
        self.slider_green = QSlider(Qt.Orientation.Horizontal)
        self.slider_green.setRange(0, 255)
        self.slider_green.setSingleStep(1)
        self.slider_green.valueChanged.connect(self.value_changed, "green")

        slider_blue_label = QLabel("Blue")
        self.slider_blue = QSlider(Qt.Orientation.Horizontal)
        self.slider_blue.setRange(0, 255)
        self.slider_blue.setSingleStep(1)
        self.slider_blue.valueChanged.connect(self.value_changed, "blue")

        for ele in [
            slider_red_label,
            self.slider_red,
            slider_green_label,
            self.slider_green,
            slider_blue_label,
            self.slider_blue,
        ]:
            self.layout.addWidget(ele)

    def value_changed(self, value, color):
        red = value if color == "red" else self.red
        green = value if color == "green" else self.green
        blue = value if color == "blue" else self.blue

        self.updateColor(red, green, blue)
        color_dict = {"red": red, "green": green, "blue": blue}
        self.update_color_values(color_dict)

    def update_color_values(self, color_dict):
        self.red = color_dict["red"]
        self.green = color_dict["green"]
        self.blue = color_dict["blue"]
