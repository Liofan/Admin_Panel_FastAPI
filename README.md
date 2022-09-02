# API для воды


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Реализованно:

- GRUD Товары
- Связь между таблицами
- Получения тары по обьему
- Добавить еще связь таблицу "Страна"
- Добавить GRUD таблицы "Коды" "Групповые коды"
- Добавить пользователей
- Авторизацию по токену

## В планах

- Создать схемы для красивого вывода
- Разделение пользователей на роли доступа к GRUD 
- Пагинация
- Загрузка кодов через файл csv
- Групповые коды
- Ящики


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