import csv
import os
from collections import defaultdict
from datetime import datetime

from .constants import RESULTS_DIR_PATH


class PepParsePipeline:
    def __init__(self):
        os.makedirs(RESULTS_DIR_PATH, exist_ok=True)

    def open_spider(self, spider):
        self.counter = defaultdict(int)

    def process_item(self, item, spider):
        status = item['status']
        self.counter[status] += 1
        return item

    def close_spider(self, spider):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'status_summary_{timestamp}.csv'
        file_path = RESULTS_DIR_PATH / file_name
        with open(file_path, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, dialect='unix')
            results = (
                ('Статус', 'Количество'),
                *self.counter.items(),
                ('Total', sum(self.counter.values()))
            )
            writer.writerows(results)
