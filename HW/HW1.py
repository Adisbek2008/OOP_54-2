class Person():

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой age {self.age} , мой city {self.city}")

    def is_adult(self):
        if self.age >= 18:
            print(True)
        else:
            print(False)

# Задание №1
name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
city = input("Введите название вашего города: ")


policeman = Person(name = name, age = age, city = city)
policeman.introduce()

# Задание №2
name2 = input("Введите ваше имя: ")
age2 = int(input("Введите ваш возраст: "))
city2 = input("Введите название вашего города: ")

another_people = Person(name = name2, age = age2, city = city2)
another_people.is_adult()