from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QStackedLayout,
)
from PySide6.QtCore import Qt, QEvent, QThread

from src.components.shape import ShapeWidget
from src.components.ui import OptionBox, TextBubble, Menu
from src.components.ui.option_controller import ShapeController
from src.speech.detect_talk import DetectTalk


class FloatingWindow(QMainWindow):
    def __init__(self, audio_map={}):
        super().__init__()

        ### Remove popup box and the close (X) and minimize (-) icons
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)

        ### Make the application transparent.
        self.setAttribute(Qt.WA_TranslucentBackground)

        ### Main container for the whole application
        container = QWidget()
        ### Layout setting
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(container)

        ### Stack container
        self.left_container = QWidget()
        left_layout = QStackedLayout(self.left_container)
        left_layout.setStackingMode(QStackedLayout.StackAll)
        left_layout.setAlignment(Qt.AlignTop)
        layout.addWidget(self.left_container)

        ### Shape
        self.shape_widget = ShapeWidget()
        self.left_container.installEventFilter(self)
        left_layout.addWidget(self.shape_widget)

        ### Textbox
        self.text_bubble = TextBubble()
        ### Textbox container
        textbox_container = QWidget()
        textbox_layout = QVBoxLayout()
        textbox_container.setLayout(textbox_layout)
        textbox_layout.addStretch()  # Move the textbox to the bottom of the application
        textbox_layout.addWidget(self.text_bubble)
        left_layout.addWidget(textbox_container)
        textbox_container.raise_()  # Always on top of the stack

        ### Menu container
        self.menu_container = QWidget()
        menu_layout = QVBoxLayout(self.menu_container)
        menu_layout.setAlignment(Qt.AlignTop)
        layout.addWidget(self.menu_container)
        ### Menu
        self.menu = Menu()
        self.menu.toggleOptionUi.connect(self.toggle_option_ui)
        menu_layout.addWidget(self.menu, alignment=Qt.AlignLeft)

        ### Option
        self.option_ui = OptionBox()
        self.option_ui.setVisible(False)
        menu_layout.addWidget(self.option_ui)

        ### Shape Controller
        self.shape_controller = ShapeController(self.shape_widget)
        self.option_ui.shapeSelected.connect(
            lambda selected_shape: self.handle_shape_controller(
                "switch_shape", selected_shape
            )
        )
        self.option_ui.randomColor.connect(
            lambda: self.handle_shape_controller("random_color")
        )

        self.option_ui.quitApplication.connect(self.close_application)
        ### Voice
        self.voice_thread = QThread()
        self.voice = DetectTalk(audio_map=audio_map)
        self.voice.moveToThread(self.voice_thread)
        self.voice_thread.started.connect(self.voice.start)
        self.voice.speechEnded.connect(self.text_bubble.update_text)

        self.voice_thread.start()
        ### Response Audio list
        self.audio_map = audio_map

        ### Drag and Drop model
        self.drag_pos = None
        self.drag_enabled = False

        ### Popup setting
        self.resize(400, 300)

        self.left_container.setFixedWidth(325)

    ### Detect keyboard press to end application
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.closeVoiceThread()
            QApplication.quit()

    ### Quit/Stop application
    def close_application(self):
        self.closeVoiceThread()
        QApplication.quit()

    ### Drag and Drop event
    def eventFilter(self, watched, event):
        if watched is self.left_container:
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

    ### Handle shape controller
    def handle_shape_controller(self, action, value=""):
        if action == "switch_shape":
            self.shape_controller.switch_shape(value)
        elif action == "random_color":
            self.shape_controller.random_color()

    ### Close QThread when application close
    def closeVoiceThread(self):
        if hasattr(self, "voice_thread"):
            self.voice_thread.quit()
            self.voice_thread.wait()

    def toggle_option_ui(self):
        self.option_ui.setVisible(not self.option_ui.isVisible())
