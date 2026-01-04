from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal
from .layout_base import LayoutBase


class OptionUI(LayoutBase):
    randomColor = Signal()
    quitApplication = Signal()
    modelsOptionButton = Signal()

    def __init__(self):

        self.btn_models = QPushButton("Models")
        self.btn_models.clicked.connect(lambda: self.modelsOptionButton.emit())
        # Random Color
        self.btn_random_color = QPushButton("Random Color")
        self.btn_random_color.clicked.connect(lambda: self.randomColor.emit())
        # Quit Application
        self.btn_quit_application = QPushButton("Quit Application")
        self.btn_quit_application.clicked.connect(lambda: self.quitApplication.emit())

        title = "Shape Controls"
        buttons_list = [
            self.btn_models,
            self.btn_random_color,
            self.btn_quit_application,
        ]
        super().__init__(title=title, buttons_list=buttons_list)
