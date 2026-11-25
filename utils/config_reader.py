"""Reads settings from resources/config/config.ini."""
import configparser
from pathlib import Path

_CONFIG_FILE = Path(__file__).resolve().parent.parent / "resources" / "config" / "config.ini"

_parser = configparser.ConfigParser()
_parser.read(_CONFIG_FILE)


def get(section, key):
    """Return a config value, e.g. get('app', 'base_url')."""
    return _parser.get(section, key)