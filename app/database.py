import cx_Oracle
from config import Config

# Функция для подключения к базе данных Oracle
def get_db_connection():
    dsn = cx_Oracle.makedsn('localhost', '1521', service_name='XEPDB1')
    conn = cx_Oracle.connect(user='my_app', password='my_password', dsn=dsn)
    return conn

# Добавление сотрудника
def add_sotrudnik(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO Sotrudnik (familiya, inmya, otchestvo, Kod_sot, Kod_dol, Kod_step, Kod_fac, stazh, Kod_prin, kabinet, Kod_caf)
    VALUES (:familiya, :inmya, :otchestvo, :Kod_sot, :Kod_dol, :Kod_step, :Kod_fac, :stazh, :Kod_prin, :kabinet, :Kod_caf)
    """

    cursor.execute(sql, data)
    conn.commit()

    cursor.close()
    conn.close()

# Удаление сотрудника
def delete_sotrudnik(sotrudnik_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "DELETE FROM Sotrudnik WHERE id = :id"

    cursor.execute(sql, [sotrudnik_id])
    conn.commit()

    cursor.close()
    conn.close()

# Обновление данных сотрудника
def update_sotrudnik(sotrudnik_id, data):
    conn = get_db_connection()
    cursor = conn.cursor()

    set_clause = ", ".join([f"{key} = :{key}" for key in data.keys()])
    sql = f"UPDATE Sotrudnik SET {set_clause} WHERE id = :id"

    data['id'] = sotrudnik_id
    cursor.execute(sql, data)
    conn.commit()

    cursor.close()
    conn.close()

# Получение списка всех сотрудников
def get_all_sotrudniki():
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "SELECT * FROM Sotrudnik"
    cursor.execute(sql)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


# Получение данных из таблиц
def get_table_data(table_name):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = f"SELECT * FROM {table_name}"
    cursor.execute(sql)

    # Получаем названия колонок
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()

    # Преобразуем каждый результат в словарь с названиями колонок в качестве ключей
    table_data = [dict(zip(columns, row)) for row in rows]

    cursor.close()
    conn.close()

    return table_data


