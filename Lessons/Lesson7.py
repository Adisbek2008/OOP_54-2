import sqlite3

# Альбом из A4 бумаги
connect = sqlite3.connect("users.db")

# Рука у которой есть карандаш
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR(30) NOT NULL, 
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')

connect.commit()


# CRUD - CREATE - READ - UPDATE - DELETE

import sqlite3

# Альбом из А4 листов
connect = sqlite3.connect("users.db")


# Рука у которой есть карандаш
cursor = connect.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR(30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
""")

connect.commit()


# CRUD - Create - Read - Update - Delete

def add_user(name: str, age: int, hobby = "None"):

    cursor.execute(
        f"INSERT INTO users(name, age, hobby) VALUES (?,?,?)",
        (name, age, hobby)
    )
    connect.commit()
    print(f"{name} - добавили")


add_user("John", 26, "Спать")

def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.f

def update_user(name, rowid):
    cursor.execute('UPDATE users SET name = ? WHERE rowid = ?'
                   (name, rowid)
    )
    connect.commit()
    print("Обновлен пользователь")

update_user('Adisbek', 3)

def delete_user(rowid):
    cursor.execute(
        "DELETE FROM users WHERE rowid = ?"
        (rowid)
    )
    connect.commit(3)

print("Пользователь удален")