import csv
import psycopg2 as pgsql

# Подключение к базе данных PostgreSQL
connection = pgsql.connect(host="localhost", dbname="postgres", user="postgres", password="bakdaulet010207", port=5432)
cur = connection.cursor()

# Создание таблицы PhoneBook, если она ещё не существует
cur.execute("""CREATE TABLE IF NOT EXISTS PhoneBook (
    surname VARCHAR(255),
    name VARCHAR(255),
    number VARCHAR(255)
);""")

# Функция для обновления записи
def update(sn, mode, newv):
    cur.execute("""UPDATE PhoneBook
    SET {} = '{}'
    WHERE surname = '{}'
    """.format(mode, newv, sn))

# Функция для удаления записи
def delete(sn):
    cur.execute("""DELETE FROM Phonebook
    WHERE surname='{}'
    """.format(sn))

# ВВОД ДАННЫХ ВРУЧНУЮ --------------------------

mode = "enter"
while True:
    print("Введите 'enter', чтобы добавить данные, или 'stop', чтобы выйти")
    mode = input()
    if mode == "stop":
        break
    mytuple = []
    print("Введите фамилию:")
    mytuple.append(input())
    print("Введите имя:")
    mytuple.append(input())
    print("Введите номер телефона:")
    mytuple.append(input())
    mytuple = tuple(mytuple)
    cur.execute("""INSERT INTO PhoneBook (surname, name, number) VALUES
    {};
    """.format(mytuple))

# ЗАГРУЗКА ДАННЫХ ИЗ CSV-ФАЙЛА ----------------
while True:
    print("Хотите загрузить данные из CSV-файла? yes/no:")
    mode = input()
    if mode == "no":
        break
    print("Введите имя файла:")
    mode = input()
    ff = 'lab10/' + mode + '.csv'
    with open(ff, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # пропустить заголовок
        for row in reader:
            cur.execute("INSERT INTO PhoneBook VALUES (%s, %s, %s)", row)

# ОБНОВЛЕНИЕ ДАННЫХ ---------------------------
while True:
    print("Введите 'update', чтобы изменить данные, или 'stop', чтобы выйти")
    mode = input()
    if mode == "stop":
        break
    cur.execute("""SELECT * FROM PhoneBook""")
    print(cur.fetchall())
    print("Введите фамилию:")
    idtochange = input()
    print("Что вы хотите изменить? name/number")
    mode = input()
    print("Введите новое значение:")
    newvalue = input()
    update(idtochange, mode, newvalue)

# УДАЛЕНИЕ ДАННЫХ -----------------------------
while True:
    print("Хотите удалить данные? yes/no")
    mode = input()
    if mode == "no":
        break
    cur.execute("""SELECT * FROM PhoneBook""")
    print(cur.fetchall())
    print("Введите фамилию:")
    idtodelete = input()
    delete(idtodelete)

# Сохранение изменений и закрытие соединения
connection.commit()
cur.close()
connection.close()
