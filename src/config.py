from dataclasses import dataclass
from pathlib import Path
import tomllib
import sys


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
class Config:
    app: AppConfig
    window: WindowConfig
    paths: PathsConfig


_CONFIG: Config | None = None


def get_app_dir() -> Path:
    if getattr(sys, "frozen", False):
        # Running as .exe
        return Path(sys.executable).parent
    # Running from source
    return Path(__file__).parent.parent


def load_config() -> Config:
    global _CONFIG
    if _CONFIG is None:
        config_path = get_app_dir() / "settings.toml"

        if not config_path.exists():
            raise RuntimeError(f"Missing settings.toml at {config_path}")

        with open(config_path, "rb") as f:
            raw = tomllib.load(f)
        _CONFIG = Config(
            app=AppConfig(**raw["app"]),
            window=WindowConfig(**raw["window"]),
            paths=PathsConfig(**raw["paths"]),
        )
    return _CONFIG


def get_config() -> Config:
    if _CONFIG is None:
        raise RuntimeError("Config not loaded. Call load_config() first.")
    return _CONFIG


def get_width() -> int:
    if _CONFIG is None:
        raise RuntimeError("Config not loaded. Call load_config() first.")
    width = _CONFIG.window.width if _CONFIG.window.width > 400 else 400
    return width


def get_height() -> int:
    if _CONFIG is None:
        raise RuntimeError("Config not loaded. Call load_config() first.")
    height = _CONFIG.window.height if _CONFIG.window.height > 300 else 300
    return height
