from PySide6.QtWidgets import QPushButton, QSlider, QLabel
from PySide6.QtCore import Qt

from .layout_base import LayoutBase


class TextOption(LayoutBase):

    def __init__(self):
        self.btn_text = QPushButton("Toggle Text")

        title = "Text Control"
        buttons_list = [self.btn_text]
        super().__init__(title=title, buttons_list=buttons_list)

        self.text_size_label = QLabel("Size")
        self.text_size = QSlider(Qt.Orientation.Horizontal)
        self.text_size.setRange(10, 30)
        self.text_size.setValue(12)
        self.text_size.valueChanged.connect(self.text_size_changed)

        self.text_size_label.setStyleSheet(
            """
                    QLabel {
                        color: white;
                    }
                """
        )

        for ele in [self.text_size_label, self.text_size]:
            self.layout.addWidget(ele)

    def text_size_changed(self, size):
        print("size")
