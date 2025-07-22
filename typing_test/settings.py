from pathlib import Path
import subprocess
import json
import os
import platform


system = platform.system()

def _get_config_file():

    if system == 'Windows':
        app_data = os.getenv('APPDATA')
        if not app_data:
            raise EnvironmentError('APPDATA environment variable not found')
        config_dir = Path(app_data) / 'pypingtest'
    elif system == 'Darwin': #MacOS
        config_dir = Path.home() / 'Library' / 'Application Support' / 'pypingtest'
    else: # Linux and other *nix
        config_dir = Path(os.getenv('XDG_CONFIG_HOME', Path.home() / '.config')) / 'pypingtest'
    
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir / 'config.json'

CONFIG_FILE = _get_config_file()

def create_default_settings():
    if not CONFIG_FILE.exists():
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

def show_config_file():
    if system == 'Windows':
        subprocess.run(['notepad', str(CONFIG_FILE)])
    else:
        editor = os.getenv('EDITOR', 'nano')
        subprocess.run([editor, str(CONFIG_FILE)])
