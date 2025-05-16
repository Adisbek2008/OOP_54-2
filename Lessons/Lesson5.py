# #Декораторы
#
# def my_decorator(func):
#
#     def wrapper():
#         print("Перед функцией")
#         print("После функции")
#         func()
#
#     return wrapper
#
# @my_decorator
# def hello():
#     print("Hello")
#
# hello()

# def repeat(n):
#
#     def decorator(func):
#
#         def wrapper():
#             for i in range(n):
#                 func()
#         return wrapper
#
#     return decorator
#
# @repeat(4)
# def hello():
#     print("Привет!!!")
#
# hello()

# def class_decorator(cls):
#
#     class NewClass(cls):
#
#         def new_method(self):
#
#             return print("Новый метод!!")
#
#     return NewClass
#
# @class_decorator
# class MyClass:
#
#     def old_method(self):
#         return print("Старый метод")
#
#
# obj = MyClass()
# obj.new_method()
#
#
#
# class Mathuntill:
#
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#
# class Person:
#
#     count = 0
#
#     def __init__(self, name):
#         # Атрибуты эксемпляра класса
#         self.name = name
#         Person.count += 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#
# b1 = Person("Test1")
# b2 = Person("Test2")
# print(Person.get_count())

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def just_method(self):
        return f"{self.first_name}, Just method"

    @property
    def test(self):
        return f"{self.first_name}"


p = Person("John", "Dru")

print(p.test)