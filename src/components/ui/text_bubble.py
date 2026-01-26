from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen, QBrush, QFont
from PySide6.QtCore import Qt

from src.config import get_window_width, get_text_size, get_text_visibilty


class TextBubble(QWidget):
    def __init__(self, text="Hello!"):
        super().__init__()
        self.setVisible(get_text_visibilty())

        self.text = text
        self.font = "Arial"
        self.font_size = get_text_size() or 12
        self.bg_color = QColor(255, 255, 255)
        self.outline_color = QColor(30, 30, 30)

        width = get_window_width()
        self.setFixedSize(width * 0.75, 120)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        rect = self.rect()
        bubble_rect = rect.adjusted(10, 10, -10, -30)

        painter.setBrush(QBrush(self.bg_color))
        painter.setPen(QPen(self.outline_color, 2))
        painter.drawRoundedRect(bubble_rect, 20, 20)
        font = QFont(self.font, self.font_size)
        painter.setFont(font)

        painter.setPen(Qt.black)
        painter.drawText(
            bubble_rect.adjusted(15, 15, -15, -15), Qt.TextWordWrap, self.text
        )

    def update_text(self, new_text):
        self.text = new_text
        self.update()

    def update_text_size(self, size):
        self.font_size = size
        self.update()

    def update_visible(self, isVisible):
        self.setVisible(isVisible)
        self.update()
