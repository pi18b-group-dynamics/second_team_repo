import sqlite3


conn = sqlite3.connect('Chinook_Sqlite.sqlite')     # подключение к бд (sqlite - нафиг локальный сервер)
cursor = conn.cursor()


cursor.execute('INSERT INTO test (first_name, last_name) VALUES ("Никита", "Куркурин")')
conn.commit()
conn.close()

