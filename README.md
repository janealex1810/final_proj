# final_proj
Дипломная работа по автоматизации

# Автотесты для Кинопоиск

## Структура проекта
- tests/ — UI и API тесты
- config/ — настройки и тестовые данные
- pages/ — PageObject классы для UI
- utils/ — фикстуры и хелперы

## Запуск
- Только UI: `pytest -m ui`
- Только API: `pytest -m api`
- Все тесты: `pytest`
- Отчёт allure: `pytest --alluredir=allure-results`