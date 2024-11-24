# main.py

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui_main import Ui_MainWindow  # Импорт интерфейса
import sqlite3
import sys

# Импортируем функции работы с БД из db.py
from db import create_db, add_user, get_users

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Создаем базу данных (если еще не создана)
        create_db()

        # Подключаем обработчик кнопки
        self.button_add.clicked.connect(self.add_user)

        # Отображаем пользователей в таблице
        self.load_users()

    def add_user(self):
        name = self.input_name.text()
        email = self.input_email.text()

        if name and email:
            # Добавляем пользователя в базу данных
            add_user(name, email)
            self.load_users()  # Обновляем таблицу

            # Очищаем поля ввода
            self.input_name.clear()
            self.input_email.clear()

    def load_users(self):
        users = get_users()

        # Очищаем таблицу перед обновлением
        self.table_users.setRowCount(0)

        # Заполняем таблицу данными
        for row, user in enumerate(users):
            self.table_users.insertRow(row)
            for col, data in enumerate(user):
                self.table_users.setItem(row, col, QTableWidgetItem(str(data)))


def main():
    app = QApplication(sys.argv)  # Создаем приложение
    window = MainWindow()          # Создаем главное окно
    window.show()                  # Показываем окно
    sys.exit(app.exec_())          # Запуск главного цикла

if __name__ == "__main__":
    main()
