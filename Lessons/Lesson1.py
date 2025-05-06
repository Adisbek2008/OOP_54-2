# класс
class Hero:

    # констурктор класса
    def __init__(self, name, level, hp):
        # атрибуты класса
        self.name = name
        self.level = level
        self.hp = hp

    # метод класса
    def action(self):
        print(f"Базовое действие {self.name_1}")


# Объект класса
kirito = Hero("Kirito", 100, 1000)
asuna = Hero(hp=98, name="Asuna", level=1000)

# kirito.action()
# asuna.action()

print(asuna.hp_1)