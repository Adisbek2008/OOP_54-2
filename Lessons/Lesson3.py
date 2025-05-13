# # Инкапсуляция
#
# import random
#
# class BankAccount:
#
#     def __init__(self, user, balance, password):
#         self.user = user # открытый
#         self._balance = balance # защищенный атрибут
#         self.__password = password # Приватный атрибут
#
#     def get_password(self):
#         return print(self.__password)
#
#     def __generate_pass(self):
#         return random.randint(1, 100)
#
#     def reset_pass(self):
#         self.__password = self.__generate_pass()
#
# john = BankAccount("John", 1000, 123321)
#
# print(john._BankAccount__password)
#

# Абстракция

# from abc import ABC, abstractmethod
#
#
# # Абстрактный класс
# class Animal(ABC):
#
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#     @abstractmethod
#     def move(self):
#         pass
#
#
# class Dog(Animal):
#
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self):
#         return print(f"{self.name} ГАВ-ГАВ")
#
#     def move(self):
#         return print(f"{self.name} move")
# tusic = Dog("Tusic")
#
# print(tusic.name)

#
# from abc import ABC, abstractmethod
#
# class SmsSend(ABC):
#
#     @abstractmethod
#     def send_otp_cod(self):
#         pass
#
#
# class KGSmsSend(SmsSend):
#
#     def jonoty(self):
#         sms = "1234"
#         return sms

print("Hello")