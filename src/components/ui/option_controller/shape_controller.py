import random

from src.components.shape import CubeWidget, ShapeWidget, SphereWidget


class ShapeController:
    def __init__(self, shape_widget: ShapeWidget):
        super().__init__()
        self.shape_widget = shape_widget

        self.shapes = {"cube": CubeWidget(), "sphere": SphereWidget()}

    def switch_shape(self, selected_shape):
        if selected_shape in self.shapes:
            self.shape_widget.set_shape(self.shapes[selected_shape])
            print("Switched to:", selected_shape)
        else:
            print(selected_shape.capitalize(), " does not exist.")

    def random_color(self):
        r = random.random()
        g = random.random()
        b = random.random()

        self.shape_widget.color = (r, g, b)
        # self.shape_widget.update()
        print(f"Shape color changed to RGB ({r}, {g}, {b}).")
