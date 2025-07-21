""""Утилитки проекта scrapy_parser_pep."""
import re
from datetime import datetime
from typing import Tuple


def get_pep_name_number(self, name: str) -> Tuple[str, str]:
    """Вытаскивает номер и название из заголовка PEPа."""
    number_pattern = r'PEP\s+(\d+)'
    name_pattern = r'^PEP \d+ – (.+)$'
    number_match = re.search(number_pattern, name)
    name_match = re.search(name_pattern, name)
    try:
        return number_match.group(1), name_match.group(1).strip()
    except Exception as e:
        self.logger.error(
            f'При попытке вытащить PEPа произошла ошибка - {str(e)}'
        )


def get_pep_file_name():
    """Формирует название файла pep."""
    timestamp = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
    filename = f'pep_{timestamp}.csv'
    return filename
