import datetime as dt
from collections import defaultdict

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT, RESULTS_DIR


class PepParsePipeline:
    """Обработка результатов парсинга."""
    def open_spider(self, spider):
        """Создание объектов для хранения результатов."""
        self.peps = defaultdict(int)
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        """Обработка элементов."""
        self.status = item['status']
        self.peps[self.status] += 1
        return item

    def close_spider(self, spider):
        """Запись результатов в csv-файл."""
        now = dt.datetime.now()
        time = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{time}.csv'
        file_path = self.results_dir / file_name
        result = self.peps.items()
        total = sum(self.peps.values())
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('Статус, Количество\n')
            for status, amount in result:
                f.write(f'{status}, {amount}\n')
            f.write(f'Total, {total}\n')
