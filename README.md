backend часть приложения...

### Конфигурации
для настройки конфигураций есть файл
```bash
.env_example
```

Далее нужно:
    - скоприовать файл
    - создать файл .env
    - ввести свои данные

### Установка зависимостей

    - alembic
    - fastapi
    - sqlalchemy
    - asyncpg
    - starlette
    - greenlet
    - uvicorn

### Запуск

запуск через uvicorn

мигпации алембик и:

```bash
uvicorn main:create_app --reload --lifespan off   
```
запуск через poetry
```bash
poetry run main.py  
```