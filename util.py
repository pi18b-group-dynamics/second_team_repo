import sqlite3


conn = sqlite3.connect('Chinook_Sqlite.sqlite')     # подключение к бд (sqlite - нафиг локальный сервер)
cursor = conn.cursor()


def add_in_db(**kwargs):
    if any(map(str.isdigit, kwargs.get('first_name'))):
        return "Введите нормальное ИМЯ"
    if any(map(str.isdigit, kwargs.get('last_name'))):
        return "Введите нормальную ФАМИЛИЮ"
    if any(map(str.isdigit, kwargs.get('patronymic'))):
        return "Введите нормальное ОТЧЕСТВО"
    if not kwargs.get('number_').isdigit():
        return "Введите нормальный НОМЕР"
    if any(map(str.isdigit, kwargs.get('sex'))):
        return "Введите нормальный ПОЛ"
    if any(map(str.isdigit, kwargs.get('whos_give'))):
        return "Введите нормальное ИЗДАНИЕ"
    if any(map(str.isalpha, kwargs.get('date_of_give'))):
        return "Введите нормальный ДАТУ"
    cursor.execute('INSERT INTO passports (first_name, last_name, patronymic, series, '
                   'number_, sex, whos_give, date_of_give) VALUES '
                   '("{}", "{}", "{}", "{}", {}, "{}", "{}", "{}")'.format
                   (kwargs.get('first_name'), kwargs.get('last_name'), kwargs.get('patronymic'), kwargs.get('series'),
                    kwargs.get('number_'), kwargs.get('sex'), kwargs.get('whos_give'), kwargs.get('date_of_give')))
    conn.commit()



def find_in_db(**kwargs):
    string = 'SELECT * FROM passports WHERE '
    for key, value in kwargs.items():
        string += f'{key} = "{value}" AND '
    else:
        string = string[:string.rfind(' AND ')]     # режем строку так как там появился лишний _AND_
    cursor.execute(string)
    print(cursor.fetchall())


# print(add_in_db('Урод', 'Фамилия', 'Отчество', 'Серия', 'asd', 'Пол', 'Кто выдал', '25.01.2020'))
print(find_in_db(last_name='Фамилия', first_name='Урод'))
