from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QStackedLayout,
)
from PySide6.QtCore import Qt, QEvent, QThread

from src.config import get_window_height, get_window_width, get_config

from src.components.model.shape import ShapeWidget
from src.components.ui import TextBubble
from src.speech.detect_talk import DetectTalk
from .menu import Menu


class FloatingWindow(QMainWindow):
    def __init__(self, audio_map={}):
        super().__init__()

        ### Remove popup box and the close (X) and minimize (-) icons
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)

        ### Make the application transparent.
        self.setAttribute(Qt.WA_TranslucentBackground)

        config = get_config()

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
        self.shape_widget = ShapeWidget(config)
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

        # ### Menu
        self.menu = Menu(self.shape_widget, self.text_bubble)
        self.menu.closeApplication.connect(self.close_application)
        layout.addWidget(self.menu)

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
        width = get_window_width()
        height = get_window_height()
        self.resize(width, height)

        self.left_container.setFixedWidth(width * 0.8125)

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

    ### Close QThread when application close
    def closeVoiceThread(self):
        if hasattr(self, "voice_thread"):
            self.voice_thread.quit()
            self.voice_thread.wait()
