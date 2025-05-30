import sqlite3

# Подключение к базе данных
connect = sqlite3.connect("users.db")
cursor = connect.cursor()


# Создание таблицы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR(30) NOT NULL, 
        age INTEGER NOT NULL,
        hobby TEXT,
        user_id INTEGER NOT NULL
    )
''')
connect.commit()

# Функция добавления пользователя
def add_user(name: str, age: int, hobby: str = "None", user_id: int = None):
    cursor.execute(
        "INSERT INTO users(name, age, hobby, user_id) VALUES (?, ?, ?, ?)",
        (name, age, hobby, user_id)
    )
    connect.commit()
    print(f"{name} - добавлен")


add_user("John", 26, "Спать", 1)
add_user("John2", 34, "Спать", 2)

# Получение всех пользователей
def get_all_users():
    cursor.execute('SELECT rowid, * FROM users')
    users = cursor.fetchall()
    for user in users:
        print(user)

# Обновление имени пользователя по rowid
def update_user(name: str, rowid: int):
    cursor.execute(
        'UPDATE users SET name = ? WHERE rowid = ?',
        (name, rowid)
    )
    connect.commit()
    print("Обновлён пользователь")

# Удаление пользователя по rowid
def delete_user(rowid: int):
    cursor.execute(
        "DELETE FROM users WHERE rowid = ?",
        (rowid,)
    )
    connect.commit()
    print("Пользователь удалён")


def get_user_by_id(user_id: int):
    cursor.execute(
        "SELECT rowid, name, age, hobby, user_id FROM users WHERE user_id = ?",
        (user_id,)
    )
    result = cursor.fetchone()
    if result:
        print("Найден пользователь:", result)
        return result
    else:
        print("Пользователь не найден")
        return None

    connect.commit()

users_id = int(input("Введите user_id: "))
get_user_by_id(users_id)
