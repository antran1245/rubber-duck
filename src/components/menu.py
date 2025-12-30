from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QSizePolicy,
    QWidget,
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon

from src.components.ui import OptionBox
from src.components.ui.option_controller import ShapeController


class Menu(QWidget):
    closeApplication = Signal()

    def __init__(self, shape_widget: QOpenGLWidget):
        super().__init__()

        # self.setSizePolicy(
        #     # horizontal
        #     QSizePolicy.Expanding,
        #     # vertical
        #     QSizePolicy.Expanding,
        # )

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

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

        layout.addWidget(
            self.menu_button,
            alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft,
        )

        ### Option
        self.option_ui = OptionBox()
        self.option_ui.setVisible(False)
        layout.addWidget(self.option_ui)

        ### Shape Controller
        self.shape_controller = ShapeController(shape_widget)
        self.option_ui.shapeSelected.connect(
            lambda selected_shape: self.handle_shape_controller(
                "switch_shape", selected_shape
            )
        )
        self.option_ui.randomColor.connect(
            lambda: self.handle_shape_controller("random_color")
        )

        self.option_ui.quitApplication.connect(lambda: self.closeApplication.emit())

        layout.addStretch(1)  # Force every widgets to the top
        self.setLayout(layout)

    def toggle_option_ui(self):
        self.option_ui.setVisible(not self.option_ui.isVisible())

    ### Handle shape controller
    def handle_shape_controller(self, action, value=""):
        if action == "switch_shape":
            self.shape_controller.switch_shape(value)
        elif action == "random_color":
            self.shape_controller.random_color()
