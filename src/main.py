import sys
import json
from pathlib import Path
from PySide6.QtWidgets import QApplication

from src.components.floating_window import FloatingWindow
from src.config import load_config
from src.utils.resources import resource_path

AUDIO_DIR = resource_path("assets/audio")


def main():
    try:
        with open(AUDIO_DIR / "audio_map.json", encoding="utf-8") as f:
            audio_map = json.load(f)
        app = QApplication(sys.argv)
        load_config()
        win = FloatingWindow(audio_map)
        win.show()
        sys.exit(app.exec())

    except KeyboardInterrupt:
        pass  # clean exit when pressing CTRL+C
