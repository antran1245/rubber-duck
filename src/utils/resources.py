import sys
from pathlib import Path


def resource_path(relative_path: str) -> Path:
    """
    Returns the absolute path to a resource, works in development and PyInstaller EXE.
    `relative_path` is relative to `src/` folder.
    """
    if hasattr(sys, "_MEIPASS"):
        # Running in PyInstaller EXE
        base_path = Path(sys._MEIPASS)
    else:
        # Running in development
        base_path = Path(__file__).parent.parent  # Goes up from utils/ to src/
    return base_path / relative_path
