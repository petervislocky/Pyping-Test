from pathlib import Path
import json
import os
import platform


def _get_config_file():
    system = platform.system()

    if system == 'Windows':
        config_dir = Path(os.getenv('APPDATA')) / 'pypingtest'
    elif system == 'Darwin': #MacOS
        config_dir = Path.home() / 'Library' / 'Application Support' / 'pypingtest'
    else: # Linux and other *nix
        config_dir = Path(os.getenv('XDG_CONFIG_HOME', Path.home() / '.config')) / 'pypingtest'
    
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir / 'config.json'

CONFIG_FILE = _get_config_file()

def create_default_settings():
    settings = {
        "word_count": 30
    }
    with CONFIG_FILE.open('w') as file:
        json.dump(settings, file, indent=4)


def write_settings(ref_text_length):
    settings = {
        "word_count": ref_text_length
    }
    with CONFIG_FILE.open('w') as file:
        json.dump(settings, file, indent=4)

def read_settings():
    if not CONFIG_FILE:
        create_default_settings()
    with CONFIG_FILE.open('r') as file:
        return json.load(file)