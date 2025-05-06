# # верблюжая нотация
# # змеиная нотация
#
# # WarriorHero
# # warrior_hero
#
#
# # Наследования
#
# # Родительский класс или же SuperClass, нету скобок
# class Hero:
#
#     def __init__(self, name, lvl, hp):
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp
#
#     def introdiction(self):
#         return print(f"Я {self.name}, мой уровень {self.lvl}")
#
#     def action(self):
#         return print(f"{self.name}, выполняет базовое действие")
#
# hero = Hero("Test", 100, 100)
#
# # Дочерный класс наследуют от родительского класса
# class MagicHero(Hero):
#
#     # полиформизм
#     def __init__(self, name, lvl, hp, mp):
#         super().__init__(name, lvl, hp)
#         self.mp = mp
#
#     def castom_spell(self):
#         return print(f"Кастую огонь")
#
# # полиформизм
#     def action(self):
#         return print(f"{self.name} ничего не делает")
#
# merge_hero = MagicHero("Test", 100, 100, 1000)
# merge_hero.action()

#        Множественное наследования
# class A:
#
#     def method_a(self):
#         return "A"
#
# class B(A):
#
#     def method_b(self):
#         return "B"
#
# class C(B):
#     def method_c(self):
#         return "C"
#
# test = C()
#
# print(test.method_a())

# diomond problem

class Animal:
    def action(self):
        return print("Animal action")

class swim(Animal):
    def action(self):
        super().action()
        # return print("Swim action")

class fly(Animal):
    def action(self):
        super().action()
        # return print("Fly action")


# первый вхожденный action
class duck(fly, swim):
    pass

donald_duck = duck()

donald_duck.action()

print(duck.mro())