from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QWidget,
)
from PySide6.QtCore import Qt

from src.components.shape import ShapeWidget
from src.components.ui import OptionBox
from src.components.ui.option_controller import ShapeController


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
        self.setCentralWidget(container)

        ### Shape
        self.shape_widget = ShapeWidget()
        layout.addWidget(self.shape_widget, 1)

        ### Option
        self.option_ui = OptionBox()
        layout.addWidget(self.option_ui, 0)

        ### Shape Controller
        self.shape_controller = ShapeController(self.shape_widget)
        self.option_ui.shapeSelected.connect(self.shape_controller.switch_shape)
        self.option_ui.randomColor.connect(self.shape_controller.random_color)

        self.option_ui.quitApplication.connect(self.close_application)

        ### Popup setting
        self.resize(400, 300)

    ### Detect keyboard press to end application
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            QApplication.quit()

    def close_application(self):
        QApplication.quit()
