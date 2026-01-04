from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QWidget,
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon

from src.components.ui import OptionUI, ModelsOptionButton
from src.components.ui.option_controller import ShapeController


class Menu(QWidget):
    closeApplication = Signal()

    def __init__(self, shape_widget: QOpenGLWidget):
        super().__init__()

        ### Icons
        self.icon_cog = QIcon("src/assets/icons/cog.svg")
        self.icon_close = QIcon("src/assets/icons/close.svg")
        self.icon_back = QIcon("src/assets/icons/back.svg")

        ### Menu layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        ### Menu container for buttons
        menu_container = QWidget()
        menu_layout = QHBoxLayout(menu_container)
        # menu_layout.setSpacing(0)

        ### Menu button
        self.btn_menu = QPushButton()
        self.btn_menu.setIcon(self.icon_cog)
        self.btn_menu.clicked.connect(self.toggle_option_ui)

        menu_layout.addWidget(
            self.btn_menu,
            alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft,
        )

        ### Back button
        self.btn_back = QPushButton()
        self.btn_back.setVisible(False)
        self.btn_back.setIcon(self.icon_back)
        self.btn_back.clicked.connect(self.toggle_option_ui)

        menu_layout.addWidget(
            self.btn_back,
            alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft,
        )

        for btn in [self.btn_back, self.btn_menu]:
            btn.setStyleSheet(
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

        menu_layout.addStretch(1)
        layout.addWidget(menu_container)

        ### Option
        self.option_ui = OptionUI()
        self.option_ui.setVisible(False)
        layout.addWidget(self.option_ui)

        self.models_option_button = ModelsOptionButton()
        self.models_option_button.setVisible(False)
        layout.addWidget(self.models_option_button)

        ### Shape Controller
        self.shape_controller = ShapeController(shape_widget)
        self.models_option_button.shapeSelected.connect(
            lambda selected_shape: self.handle_shape_controller(
                "switch_shape", selected_shape
            )
        )
        self.option_ui.randomColor.connect(
            lambda: self.handle_shape_controller("random_color")
        )

        self.option_ui.modelsOptionButton.connect(self.toggle_models_option_button)
        self.option_ui.quitApplication.connect(lambda: self.closeApplication.emit())

        layout.addStretch(1)  # Force every widgets to the top
        self.setLayout(layout)

    def toggle_option_ui(self):
        if not self.btn_menu.isVisible():
            self.btn_menu.setVisible(True)
        self.models_option_button.setVisible(False)
        self.btn_back.setVisible(False)
        self.option_ui.setVisible(not self.option_ui.isVisible())
        if self.option_ui.isVisible():
            self.btn_menu.setIcon(self.icon_close)
        else:
            self.btn_menu.setIcon(self.icon_cog)

    def toggle_models_option_button(self):
        self.btn_menu.setVisible(False)
        self.option_ui.setVisible(False)
        self.btn_back.setVisible(True)
        self.models_option_button.setVisible(not self.models_option_button.isVisible())

    ### Handle shape controller
    def handle_shape_controller(self, action, value=""):
        if action == "switch_shape":
            self.shape_controller.switch_shape(value)
        elif action == "random_color":
            self.shape_controller.random_color()
