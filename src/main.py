import sys
from PySide6.QtWidgets import QApplication
from src.components.floating_window import FloatingWindow


def main():
    try:
        app = QApplication(sys.argv)
        win = FloatingWindow()
        win.show()
        sys.exit(app.exec())

    except KeyboardInterrupt:
        pass  # clean exit when pressing CTRL+C
