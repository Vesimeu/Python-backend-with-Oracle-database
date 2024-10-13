import cx_Oracle

# Установите параметры подключения
dsn_tns = cx_Oracle.makedsn('localhost', 1521, service_name='XEPDB1')
connection = cx_Oracle.connect(user='my_app', password='my_password', dsn=dsn_tns)

# Создаем курсор для выполнения запросов
cursor = connection.cursor()

# Выполним простой запрос для проверки подключения
cursor.execute('SELECT * FROM Sotrudnik')

# Извлекаем и выводим результаты
for row in cursor:
    print(row)

# Закрываем подключение
cursor.close()
connection.close()
