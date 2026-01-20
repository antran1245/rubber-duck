from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal
from .layout_base import LayoutBase


class OptionUI(LayoutBase):
    modelsOptionButton = Signal()
    textOptionButton = Signal()
    quitApplication = Signal()

    def __init__(self):

        self.btn_models = QPushButton("Models")
        self.btn_models.clicked.connect(lambda: self.modelsOptionButton.emit())

        self.btn_text = QPushButton("Text")
        self.btn_text.clicked.connect(lambda: self.textOptionButton.emit())

        # Quit Application
        self.btn_quit_application = QPushButton("Quit Application")
        self.btn_quit_application.clicked.connect(lambda: self.quitApplication.emit())

        title = "Shape Control"
        buttons_list = [
            self.btn_models,
            self.btn_text,
            self.btn_quit_application,
        ]
        super().__init__(title=title, buttons_list=buttons_list)
