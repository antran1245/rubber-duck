from PySide6.QtWidgets import QHBoxLayout, QPushButton, QSizePolicy, QWidget
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon


class Menu(QWidget):
    toggleOptionUi = Signal()

    def __init__(self):
        super().__init__()

        self.setSizePolicy(
            # horizontal
            QSizePolicy.Expanding,
            # vertical
            QSizePolicy.Fixed,
        )

        layout = QHBoxLayout()

        self.menu_button = QPushButton()
        self.menu_button.setIcon(QIcon("src/assets/icons/cog.svg"))
        self.menu_button.clicked.connect(self.toggle_option_ui)
        self.menu_button.setStyleSheet(
            """
          QPushButton {
            background: white;
            padding: 3px;
            border: 2px;
            border-radius: 8px;
          }
          QPushButton:hover {
            background: rgba(60,60,60,200);
          }
          """
        )

        layout.addWidget(self.menu_button)
        self.setLayout(layout)

    def toggle_option_ui(self):
        self.toggleOptionUi.emit()
