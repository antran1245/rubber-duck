import sys
import os
from pathlib import Path
from PySide6.QtWidgets import QApplication
from src.components.floating_window import FloatingWindow

AUDIO_DIR = Path("src/assets/audio")


def main():
    try:
        audio_files = list(AUDIO_DIR.glob("*.mp3"))
        app = QApplication(sys.argv)
        win = FloatingWindow(audio_files)
        win.show()
        sys.exit(app.exec())

    except KeyboardInterrupt:
        pass  # clean exit when pressing CTRL+C
