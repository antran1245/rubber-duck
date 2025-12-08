from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QWidget,
)
from PySide6.QtCore import Qt, QEvent

from src.components.shape import ShapeWidget
from src.components.ui import OptionBox
from src.components.ui.option_controller import ShapeController


class FloatingWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ### Remove popup box and the close (X) and minimize (-) icons
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)

        ### Make the application transparent.
        self.setAttribute(Qt.WA_TranslucentBackground)

        ### Container for the whole application
        container = QWidget()
        ### Layout setting
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(container)

        ### Shape
        self.shape_widget = ShapeWidget()
        self.shape_widget.installEventFilter(self)
        layout.addWidget(self.shape_widget, 1)

        ### Option
        self.option_ui = OptionBox()
        layout.addWidget(self.option_ui, 0)

        ### Shape Controller
        self.shape_controller = ShapeController(self.shape_widget)
        self.option_ui.shapeSelected.connect(self.shape_controller.switch_shape)
        self.option_ui.randomColor.connect(self.shape_controller.random_color)

        self.option_ui.quitApplication.connect(self.close_application)

        ### Drag and Drop model
        self.drag_pos = None
        self.drag_enabled = False

        ### Popup setting
        self.resize(400, 300)

    ### Detect keyboard press to end application
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            QApplication.quit()

    ### Quit/Stop application
    def close_application(self):
        QApplication.quit()

    def eventFilter(self, watched, event):
        if watched is self.shape_widget:
            if event.type() == QEvent.Enter:
                self.drag_enabled = True
            elif event.type() == QEvent.Leave:
                self.drag_enabled = False
        return super().eventFilter(watched, event)

    def mousePressEvent(self, event):
        if self.drag_enabled and event.buttons() & Qt.LeftButton:
            self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.drag_pos and self.drag_enabled:
            delta = event.globalPosition().toPoint() - self.drag_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.drag_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.drag_pos = None
