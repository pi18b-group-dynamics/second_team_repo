import sqlite3


conn = sqlite3.connect('Chinook_Sqlite.sqlite')     # подключение к бд (sqlite - нафиг локальный сервер)
cursor = conn.cursor()


def add(first_name, second_name, third_name, series, number_, sex, whos_give, date_of_give):
    cursor.execute('INSERT INTO passports (first_name, last_name, patronymic, series, '
                   'number_, sex, whos_give, date_of_give) VALUES '
                   '("{}", "{}", "{}", "{}", {}, "{}", "{}", "{}")'.format
                   (first_name, second_name, third_name, series, number_, sex, whos_give, date_of_give))
    conn.commit()
    conn.close()


add('Имя', 'Фамилия', 'Отчество', 'Серия', 123, 'Пол', 'Кто выдал', 'Дата выдачи')