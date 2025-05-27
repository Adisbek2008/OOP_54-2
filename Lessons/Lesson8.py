import sqlite3

connect = sqlite3.connect("users.db")
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(
        grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject VARCAHR(100) NOT NULL,
        grade INTEGER NOT NULL,
        userid INTEGER,
        FOREIGN KEY (userid) REFERENCES users(user_id)
    )
''')
connect.commit()


def add_user(name: str, age: int, hobby="None"):

    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"{name} - Добавили")


# add_user("John", 26, "Спать")
# add_user("John2", 26, "Спать")
# add_user("John3", 26, "Спать")
# add_user("John4", 26, "Спать")


def add_grade(user_id, subject, grade):
    cursor.execute(
        'INSERT INTO grades(userid, subject, grade) VALUES (?,?,?)',
        (user_id, subject, grade)
    )
    connect.commit()

    print("Оценка за урок добавлена!!")

# add_grade(1, "Математика", 5)
# add_grade(1, "Физика", 3)
# add_grade(1, "ИЗО", 2)
# add_grade(1, "Физра", 4)
# add_grade(10, "Химия", 3)

def get_user_and_grades():

    cursor.execute('''
        SELECT users.name, grades.subject, grades.grade
        FROM users LEFT JOIN grades ON users.user_id = grades.userid
    ''')

    users = cursor.fetchall()

    for i in users:
        print(f"NAME: {i[0]}, SUBJECT: {i[1]}, GRADE: {i[2]}")

get_user_and_grades()

add_user(name="user", age=35, hobby="Footbal")
add_user(name="user2", age=34, hobby="Footbal")
add_user(name="user3", age=25, hobby="Footbal")
add_user(name="user4", age=45, hobby="Footbal")

def get_avarage_age():
    cursor.execute('''
        SELECT AVG(age) FROM users
    ''')

    user = cursor.fetchall()

    print(user)

get_avarage_age()

def create_view_highest_grade():

    cursor.execute('''
        CREATE VIEW IF NOT EXISTS view_highest_grade AS
        SELECT name, subject, grade
        FROM users JOIN grades ON users.user_id= grades.userid   
        WHERE grade = (SELECT MAX(grade) FROM grades)
        
    ''')

    print("Представление создано или обновленно")

create_view_highest_grade()

def view_highest_grade():
    cursor.execute('''
            SELECT * FROM view_highest_grade
    ''')
    users = cursor.fetchall()

view_highest_grade()