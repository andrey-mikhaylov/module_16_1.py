import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "main"

if __name__ == '__main__':
    uvicorn.run(app, reload=True)

"""
2024/02/16 00:00|Домашнее задание по теме "Основы Fast Api и маршрутизация"
Цель: научиться создавать базовую маршрутизацию для обработки данных в FastAPI.

Задача "Начало пути":
Подготовка:
Установите фреймворк FastAPI при помощи пакетного менеджера pip. Версию Python можете выбрать самостоятельно (3.9 - 3.12).

Маршрутизация:
Создайте приложение(объект) FastAPI предварительно импортировав класс для него.
2.Создайте маршрут к главной странице - "/". По нему должно выводиться сообщение "Главная страница".

3.Создайте маршрут к странице администратора - "/user/admin". По нему должно выводиться сообщение "Вы вошли как администратор".

4.Создайте маршрут к страницам пользователей используя параметр в пути - "/user/{user_id}". По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>".

5.Создайте маршрут к страницам пользователей передавая данные в адресной строке - "/user". По нему должно выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".

Пример получившегося интерфейса Swagger:



Примечания:
Все маршруты пишутся при мощи GET запроса.
Помните о важности порядка записи запросов в вашем файле.
Названия функций можете придумать самостоятельно с учётом логики прописанной в них.
"""