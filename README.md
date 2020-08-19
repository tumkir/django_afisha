# Интерактивная карта Москвы


## Как запустить

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- В корне проекта создайте `.env` файл и пропишите туда значение `SECRET_KEY` в формате `SECRET_KEY='значение'`

Получить секретный ключ Django можно командой
```bash
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
- Создайте базу данных командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).