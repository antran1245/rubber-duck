from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QWidget,
)
from PySide6.QtCore import Qt

from src.components.shape import CubeWidget
from src.components.ui import OptionBox


class FloatingWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ### Remove popup box and the close (X) and minimize (-) icons
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)

        ### Make the application transparent.
        # self.setAttribute(Qt.WA_TranslucentBackground)

        ### Container for the whole application
        container = QWidget()
        ### Layout setting
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)

        ### Initialize elements
        self.cube = CubeWidget()
        self.option_ui = OptionBox()

        ### Add elements to layout
        layout.addWidget(self.cube, 1)
        layout.addWidget(self.option_ui, 0)

        ### Popup setting
        self.setCentralWidget(container)
        self.resize(400, 300)

    ### Detect keyboard press to end application
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            QApplication.quit()
