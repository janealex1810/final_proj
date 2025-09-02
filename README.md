# final_proj
Дипломная работа по автоматизации

# Автотесты для Кинопоиск

## Структура проекта
- tests/ — UI и API тесты
- config/ — настройки и тестовые данные
- pages/ — PageObject классы для UI
- utils/ — фикстуры и хелперы

## Настройка окружения

1. Получить API ключ на https://kinopoisk.dev/
2. Прописать ваш токен в файле test_data.py
3. Установить зависимости: `pip install -r requirements.txt`

## Запуск
- Только UI: `pytest -m ui`
- Только API: `pytest -m api`
- Все тесты: `pytest`
- Отчёт allure: `pytest --alluredir=allure-results`