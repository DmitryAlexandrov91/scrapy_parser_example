"""Константы проекта pep_parse."""
from pathlib import Path


# Константы путей и названий директорий/папок.
BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR_NAME = 'results'
RESULTS_DIR_PATH = BASE_DIR / RESULTS_DIR_NAME
SPIDERS_DIR = 'pep_parse.spiders'
