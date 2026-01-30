from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from src.components.model.shape import Shape
import tomllib
import tomli_w
import sys

# ----------------
# Dataclass
# ----------------


@dataclass
class AppConfig:
    name: str
    debug: bool


@dataclass
class WindowConfig:
    width: int
    height: int


@dataclass
class PathsConfig:
    assets: str


@dataclass
class TextConfig:
    size: int
    visibility: bool


@dataclass
class ModelConfig:
    shape: Optional[str]
    model: Optional[str]
    shape_color_r: float
    shape_color_g: float
    shape_color_b: float


@dataclass
class Config:
    app: AppConfig
    window: WindowConfig
    paths: PathsConfig
    model: ModelConfig
    text: TextConfig


# ----------------
# Global
# ----------------
_CONFIG: Config | None = None


# ----------------
# Helpers
# ----------------
def get_app_dir() -> Path:
    if getattr(sys, "frozen", False):
        # Running as .exe
        return Path(sys.executable).parent
    # Running from source
    return Path(__file__).parent.parent


def ensure_config_loaded():
    if _CONFIG is None:
        raise RuntimeError("Config not loaded. Call load_config() first.")


def load_raw_data(path: Path) -> dict:
    with open(path, "rb") as f:
        return tomllib.load(f)


def save_raw_data(path: Path, data: dict):
    with open(path, "wb") as f:
        tomli_w.dump(data, f)


### File path
config_path = get_app_dir() / "settings.toml"


def update_setting(section: str, key: str, value):
    data = load_raw_data(config_path)
    data.setdefault(section, {})[key] = value
    save_raw_data(config_path, data)


# ----------------
# Loader
# ----------------
def load_config() -> Config:
    global _CONFIG
    if _CONFIG is None:

        if not config_path.exists():
            raise RuntimeError(f"Missing settings.toml at {config_path}")

        raw = load_raw_data(config_path)
        _CONFIG = Config(
            app=AppConfig(**raw["app"]),
            window=WindowConfig(**raw["window"]),
            paths=PathsConfig(**raw["paths"]),
            model=ModelConfig(**raw["model"]),
            text=TextConfig(**raw["text"]),
        )
    return _CONFIG


def get_config() -> Config:
    ensure_config_loaded()
    return _CONFIG


# ----------------
# Window
# ----------------
def get_window_width() -> int:
    ensure_config_loaded()
    width = _CONFIG.window.width if _CONFIG.window.width > 400 else 400
    return width


def get_window_height() -> int:
    ensure_config_loaded()
    height = _CONFIG.window.height if _CONFIG.window.height > 300 else 300
    return height


# ----------------
# Model
# ----------------
def set_shape(shape: str):
    ensure_config_loaded()
    update_setting("model", "shape", shape)


def get_shape() -> str:
    ensure_config_loaded()
    return _CONFIG.model.shape


def set_shape_color(r, g, b):
    ensure_config_loaded()
    update_setting("model", "shape_color_r", float(r))
    update_setting("model", "shape_color_g", float(g))
    update_setting("model", "shape_color_b", float(b))


def get_shape_color():
    ensure_config_loaded()
    return {
        "r": _CONFIG.model.shape_color_r,
        "g": _CONFIG.model.shape_color_g,
        "b": _CONFIG.model.shape_color_b,
    }


# ----------------
# Text
# ----------------
def set_text_size(size):
    update_setting("text", "size", size)


def get_text_size() -> int:
    ensure_config_loaded()
    return _CONFIG.text.size


def set_text_visibilty(isVisible):
    update_setting("text", "visibility", isVisible)


def get_text_visibilty() -> bool:
    ensure_config_loaded()
    return _CONFIG.text.visibility
