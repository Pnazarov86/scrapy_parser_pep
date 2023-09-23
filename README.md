# Асинхронный парсер PEP.

### Описание
Парсер документов PEP на базе фреймворка Scrapy. Парсер собирает информацию о статусах
PEP и сохраняет результаты в csv-файл.

### Запуск проекта на Linux:
Клонируйте репозиторий.
Создайте и активируйте виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Установите зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
### Запуск парсера:
```
scrapy crawl pep
```

____
### Автор  
Пётр Назаров  
(https://github.com/Pnazarov86)
