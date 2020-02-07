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


def check_all(first_name, second_name, third_name, series, number_, sex, whos_give, date_of_give):
    if any(map(str.isdigit, first_name)):
        return "Введите нормальное ИМЯ"
    if any(map(str.isdigit, second_name)):
        return "Введите нормальную ФАМИЛИЮ"
    if any(map(str.isdigit, third_name)):
        return "Введите нормальное ОТЧЕСТВО"
    if str(type(number_)) != "<class 'int'>":
        return "Введите нормальный НОМЕР"
    if any(map(str.isdigit, sex)):
        return "Введите нормальный ПОЛ"
    if any(map(str.isdigit, whos_give)):
        return "Введите нормальное ИЗДАНИЕ"
    if any(map(str.isalpha, date_of_give)):
        return "Введите нормальный ДАТУ"


print(check_all('qwe', 'Фамилия', 'Отчество', 'Серия', 123, 'Пол', 'Кто выдал', '25.01.2020'))
