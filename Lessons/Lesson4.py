# magic methods

class Vector:

    def init(self, x, y):
        self.x = x
        self.y = y

    def str(self):
        return "Я магическмй метод"




test   = Vector(12, 33)
print(test)