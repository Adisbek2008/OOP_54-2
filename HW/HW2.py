class Heroes:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        return print(f"Приветсвую, меня зовут {self.name}. На данный момент у вас {self.hp} здоровья.")

    def attack(self):
        return print(f"Вы произвели атаку!")

class Archer(Heroes):

    def __init__(self, arrows, precision, name, hp):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        self.arrows -= 1
        if self.precision == "Попал":
            print("Успешная атака!")
        else:
            print("Неуспешная атака!(")

    def rest(self):
        if self.arrows == 0:
            self.arrows + 5
            return print("Стрелы пополнены!")
        else:
            return print("Стрел достаточно")

    def status(self):
        return print(f"Текущее положение вашего персонажа: "
                     f"Имя - {self.name}, Здоровье - {self.hp}, "
                     f"Количество стрел - {self.arrows}, Попадания - {self.precision}")

#Задание №1
heroes = Heroes("Thor", 100)
heroes.action()
heroes.attack()

# Задание №2
accuracy = input('Введите "Попал", если ваш герой попал. А если нет то введите "Не попал". ')
archer_heroes = Archer(5, accuracy, "Legolas", 100)

archer_heroes.attack()
archer_heroes.rest()
archer_heroes.status()