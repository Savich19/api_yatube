# Проект API для Yatube
API для проекта социальной сети Yatube.

## Описание проекта

API Yatube социальной сети, в которой пользователи могут публиковать посты и просматривать сообщения других пользователей. Реализованы механизм комментариев к записям, возможность подписки на публикации интересующий авторов, регистрация пользователей. Для аутентификации используется JWT-токен.

## Стек технологий
* Python 3.7
* Django 2.2.16
* Django Rest Framework 3.12.4
* Pytest 6.2.4
* Simple-JWT 1.7.2

## Инструкция по запуску проекта
* Склонировать репозиторий на локальную машину:
```bash
git clone git@github.com:Savich19/api_yatube.git
cd api_yatube
```

* Cоздать и активировать виртуальное окружение:

```bash
python -m venv env
```

```bash
source venv/Scripts/activate
```

* Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

* Выполнить миграции:

```bash
python manage.py migrate
```

* Запустить проект:
```bash
python manage.py runserver
```

## Документация для Yatube API доступна по адресу
```bash
http://127.0.0.1/redoc/
```

## Автор
[Савич А.В.](https://github.com/Savich19)
