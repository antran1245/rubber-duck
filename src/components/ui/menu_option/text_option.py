from PySide6.QtWidgets import QPushButton, QSlider, QLabel, QWidget
from PySide6.QtCore import Qt

from src.config import set_text_size, set_text_visibilty
from .layout_base import LayoutBase


class TextOption(LayoutBase):

    def __init__(self, text_bubble: QWidget):
        self.text_bubble = text_bubble

        self.btn_text = QPushButton("Toggle Text")
        self.btn_text.clicked.connect(lambda: self.update_visibility())

        title = "Text Control"
        buttons_list = [self.btn_text]
        super().__init__(title=title, buttons_list=buttons_list)

        self.text_size_label = QLabel("Size")
        self.text_size = QSlider(Qt.Orientation.Horizontal)
        self.text_size.setRange(10, 32)
        self.text_size.setValue(12)
        self.text_size.valueChanged.connect(lambda value: self.update_size(value))

        self.text_size_label.setStyleSheet(
            """
                    QLabel {
                        color: white;
                    }
                """
        )

        for ele in [self.text_size_label, self.text_size]:
            self.layout.addWidget(ele)

    def update_size(self, value):
        self.text_bubble.update_text_size(value)
        set_text_size(value)

    def update_visibility(self):
        isVisible = not self.text_bubble.isVisible()
        self.text_bubble.update_visible(isVisible)
        set_text_visibilty(isVisible)
