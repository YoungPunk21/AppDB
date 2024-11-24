# Приложение для работы с базой данных пользователей на PyQt5 и SQLite

Это простое десктопное приложение, созданное с использованием **PyQt5** для графического интерфейса (GUI) и **SQLite** в качестве базы данных. Приложение позволяет пользователям добавлять свои данные (имя и email) в локальную базу данных SQLite и просматривать все записи в таблице.

## Функции приложения
- **Добавление пользователя**: Пользователи могут ввести свое имя и email и добавить их в базу данных.
- **Отображение пользователей**: Все данные, добавленные в базу, отображаются в таблице.
- **SQLite база данных**: Данные сохраняются локально в базе данных SQLite.

## Стек технологий
- **Python 3.x**
- **PyQt5** — для создания графического интерфейса.
- **SQLite** — для хранения данных (встроенная база данных в Python).

## Как запустить

### Шаг 1: Клонировать репозиторий (если используется Git)

git clone [https://github.com/yourusername/user-database-app.git](https://github.com/YoungPunk21/AppDB.git)


### Шаг 2: Установить зависимости
Для установки библиотеки PyQt5 используйте pip:

pip install pyqt5

### Шаг 3: Запуск приложения
После установки зависимостей запустите приложение командой:

python main.py

## Как работает приложение
При запуске приложения создается база данных SQLite (если она еще не существует) с таблицей пользователей.
В графическом интерфейсе есть поля для ввода имени и email пользователя, а также кнопка для добавления данных в базу.
Все добавленные пользователи отображаются в таблице на экране.
