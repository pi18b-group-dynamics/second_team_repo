import datetime
import re
import sqlite3


conn = sqlite3.connect('Chinook_Sqlite.sqlite')     # подключение к бд (sqlite - нафиг локальный сервер)
cursor = conn.cursor()


def check_all(**kwargs):
    if not kwargs.get('first_name') or any(map(str.isdigit, kwargs.get('first_name'))):
        return "Введите нормальное ИМЯ", 'first_name'
    if not kwargs.get('last_name') or any(map(str.isdigit, kwargs.get('last_name'))):
        return "Введите нормальную ФАМИЛИЮ", 'last_name'
    if not kwargs.get('patronymic') or any(map(str.isdigit, kwargs.get('patronymic'))):
        return "Введите нормальное ОТЧЕСТВО", 'patronymic'
    if not kwargs.get('number_').isdigit():
        return "Введите нормальный НОМЕР", 'number_'
    if not kwargs.get('sex') or any(map(str.isdigit, kwargs.get('sex'))):
        return "Введите нормальный ПОЛ", 'sex'
    if not kwargs.get('whos_give') or any(map(str.isdigit, kwargs.get('whos_give'))):
        return "Введите нормальное ИЗДАНИЕ", 'whos_give'
    try:
        datetime.datetime.strptime(kwargs.get('date_of_give'), '%d.%m.%Y')
    except:
        return "Введите нормальный ДАТУ", 'date_of_give'
    return True


def add_in_db(**kwargs):
    result = check_all(**kwargs)
    if result is True:
        cursor.execute('INSERT INTO passports (first_name, last_name, patronymic, series, '
                       'number_, sex, whos_give, date_of_give, photo) VALUES '
                       '("{}", "{}", "{}", "{}", {}, "{}", "{}", "{}", "{}")'.format
                       (kwargs.get('first_name'), kwargs.get('last_name'), kwargs.get('patronymic'), kwargs.get('series'),
                        kwargs.get('number_'), kwargs.get('sex'), kwargs.get('whos_give'), kwargs.get('date_of_give'), kwargs.get('photo')))
        conn.commit()
        return 'Запись добавлена'
    else:
        return result


def find_in_db(**kwargs):
    string = 'SELECT * FROM passports WHERE '
    for key, value in kwargs.items():
        if value:
            string += f'{key} = "{value}" AND '
    else:
        if len(string) == 30:
            return None
        string = string[:string.rfind(' AND ')]     # режем строку так как там появился лишний _AND_
    cursor.execute(string)
    return cursor.fetchall()


def print_pic(id):
    return cursor.execute(f'SELECT photo FROM passports WHERE id = "{id}"').fetchall()[0][0]


if __name__ == '__main__':
    # print(add_in_db('Урод', 'Фамилия', 'Отчество', 'Серия', 'asd', 'Пол', 'Кто выдал', '25.01.2020'))
    pass


def remove_from_db(data):
    """
        Удаление из бд,
    :param data: данные которые ввел пользователь
    :return:
    """
    if len(data) == 0:
        return 'Удаление не произошло'
    query = 'DELETE FROM passports WHERE '
    for field, value in data.items():
        if value:
            query += field + ' = "' + value + '" AND '
    else:
        query = query[:-4]
    cursor.execute(query)
    conn.commit()
    return 'Удаление успешно'


def check_in_db(data):
    """
        Прозводим проверку человека, есть ли он в базе,(для изменения данных человека)
        :param data: данные которые ввел пользователь
        :return:
    """
    query = 'SELECT * ' \
            'FROM passports ' \
            'WHERE '
    for field, value in data.items():
        if value:
            query += field + ' = "' + value + '" AND '
    else:
        query = query[:-4]
    return bool(cursor.execute(query).fetchall())


def check_on_of_all(kwargs):
    if kwargs.get('first_name') or any(map(str.isdigit, kwargs.get('first_name'))):
        return False
    if kwargs.get('last_name') or any(map(str.isdigit, kwargs.get('last_name'))):
        return False
    if kwargs.get('patronymic') or any(map(str.isdigit, kwargs.get('patronymic'))):
        return False
    if kwargs.get('number_').isdigit():
        return False
    if kwargs.get('sex') or any(map(str.isdigit, kwargs.get('sex'))):
        return False
    if kwargs.get('whos_give') or any(map(str.isdigit, kwargs.get('whos_give'))):
        return False
    if kwargs.get('date_of_give'):
        try:
            datetime.datetime.strptime(kwargs.get('date_of_give'), '%d.%m.%Y')
        except:
            return False
    return True


def print_all():
    return cursor.execute('SELECT * FROM passports').fetchall()
