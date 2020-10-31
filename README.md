# Интерактивная карта Москвы

Cайт о самых интересных местах в Москве. [Пример работающего проекта](http://tumkir.pythonanywhere.com/)

## Как запустить

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- В корне проекта создайте `.env` файл и пропишите туда переменные окружения:
  - [`SECRET_KEY`](https://docs.djangoproject.com/en/3.1/ref/settings/#secret-key) в формате `SECRET_KEY='значение'`
  - [`DEBUG`](https://docs.djangoproject.com/en/3.1/ref/settings/#debug) — впишите `True` для включения дебаг-режима
  - [`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts) — адрес хоста/домена, для которых может работать текущий сайт. Если проект при запуске выдаёт ошибку `Bad Request (400)`, то скорее всего причина в неверно прописанном параметре `ALLOWED_HOSTS`. Несколько хостов прописываются просто через запятую, без пробелов и кавычек `ALLOWED_HOSTS = 127.0.0.1,example.com`.

Получить секретный ключ Django можно командой
```bash
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
- Создайте базу данных командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

