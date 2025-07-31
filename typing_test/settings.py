from pathlib import Path
import subprocess
import json
import os
import platform
from typing import Any


system = platform.system()


def _get_config_file() -> Path:
    """Creates a path for the config file based on user OS"""
    if system == "Windows":
        app_data = os.getenv("APPDATA")
        if not app_data:
            raise EnvironmentError("APPDATA environment variable not found")
        config_dir = Path(app_data) / "pypingtest"
    elif system == "Darwin":  # MacOS
        config_dir = Path.home() / "Library" / "Application Support" / "pypingtest"
    else:  # Linux and other *nix
        config_dir = (
            Path(os.getenv("XDG_CONFIG_HOME", Path.home() / ".config")) / "pypingtest"
        )

    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir / "config.json"


CONFIG_FILE = _get_config_file()


# TODO: Create a setting block for timed mode time
def create_default_settings() -> None:
    if not CONFIG_FILE.exists():
        settings = {"word_count": 30, "difficulty": "medium", "mode": "perfect"}
        with CONFIG_FILE.open("w") as file:
            json.dump(settings, file, indent=4)


def read_settings() -> dict[str, Any]:
    with CONFIG_FILE.open("r") as file:
        return json.load(file)


def show_config_file() -> None:
    if system == "Windows":
        subprocess.run(["notepad", str(CONFIG_FILE)])
    else:
        editor = os.getenv("EDITOR", "nano")
        subprocess.run([editor, str(CONFIG_FILE)])


def check_settings_validity(settings: dict[str, Any]) -> None:

    class InvalidSettingsError(Exception):
        """Raises an exception when there are invalid settings in the
        config file"""

        pass

    def word_count_validity(word_count: int) -> None:
        if not (5 <= word_count <= 300):
            raise InvalidSettingsError(
                f"Config error: word_count length must be > 5 and > 300"
            )

    def difficulty_validity(difficulty: str) -> None:
        if difficulty not in ("easy", "medium", "hard", "veryHard"):
            raise InvalidSettingsError(
                f"Config error: invalid difficulty setting {difficulty}, "
                "options are easy, medium, hard, or veryHard"
            )

    def mode_validity(mode: str) -> None:
        if mode not in ("perfect", "timed"):
            raise InvalidSettingsError(
                f"Config error: invalid mode setting {mode}, "
                "options are perfect or timed"
            )

    valid_settings = ["word_count", "difficulty", "mode"]
    for key in valid_settings:
        if key not in settings:
            raise InvalidSettingsError(
                f"Config error: required key {key} missing from config file"
            )

    word_count_validity(settings["word_count"])
    difficulty_validity(settings["difficulty"])
    mode_validity(settings["mode"])
