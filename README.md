# Admin Panel FastAPI

## _The Last Markdown Editor, Ever_


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Реализованно:

- GRUD Товары
- Связь между таблицами
- Получения тары по обьему
- Добавить еще связь таблицу "Страна"
- Добавить GRUD таблицы "Коды" "Групповые коды"

## В планах

- Создать схемы для красивого вывода

- Добавить пользователей
- Авторизацию по токену
- Разделение пользователей на роли доступа к GRUD 
- Загрузка кодов через файл csv


## Установка


Создайте виртуальное окружение и активируйте его

```sh
python -m venv venv
.\venv\Scripts\activate
```
Установите зависимости

```sh
pip install -r requirements.txt
```

Создайте файл .env и добавьте ссылку на БД

```sh
DATABASE_URl_PSQL = postgresql://login:password@localhost:port/db
```


Запустите проект

```sh
python main.py
```

Перейдите по адресу [Link]
```sh
http://127.0.0.1:8080/docs
```



## Docker

В планах развернуть все в докере


[Link]: <http://127.0.0.1:8080/docs>