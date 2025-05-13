from random import randint

class Student:

    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    def set_grade(self):
        self.__grade = randint(0, 100)

    def get_grade(self):
        return print(self.__grade)

    def get_info(self):
        return print(f"Имя: {self.__name}, Оценка: {self.__grade}")


student = Student("Ivan", 65)
student.get_info()
student.set_grade()
student.get_info()


from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):

    def __init__(self, side):
        self.side = side


    def area(self):
        return side * side

