import sqlite3


conn = sqlite3.connect('Chinook_Sqlite.sqlite')     # подключение к бд (sqlite - нафиг локальный сервер)
cursor = conn.cursor()


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
    cursor.execute('INSERT INTO passports (first_name, last_name, patronymic, series, '
                   'number_, sex, whos_give, date_of_give) VALUES '
                   '("{}", "{}", "{}", "{}", {}, "{}", "{}", "{}")'.format
                   (first_name, second_name, third_name, series, number_, sex, whos_give, date_of_give))
    conn.commit()
    conn.close()


print(check_all('Урод', 'Фамилия', 'Отчество', 'Серия', 'asd', 'Пол', 'Кто выдал', '25.01.2020'))
