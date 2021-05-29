import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)  # площадь окружности

    def perimeter(self):
        return 2 * math.pi * self.radius  # периметр окружности

    def concentrichnost(self, cir):  # концентричность окружностей
        if self.x == cir.x & self.y == cir.y:
            print('Окружности концентричны')
        else:
            print('Окружности не концентричны')

    def persechenie(self, cir):  # пересечение окружностей
        if self.x == cir.x:
            if self.radius + cir.radius > abs(self.y - cir.y):
                print('Окружности пересекаются')
            else:
                print('Окружности не пересекаются')
        elif self.y == cir.y:
            if self.radius + cir.radius > abs(self.x - cir.x):
                print('Окружности пересекаются')
            else:
                print('Окружности не пересекаются')
        else:
            if (self.radius + cir.radius) ** 2 > abs((self.x - cir.x) ** 2 - (self.y - cir.y) ** 2):
                print('Окружности пересекаются')
            else:
                print('Окружности не пересекаются')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cir1 = Circle(3, 5, 3)
    cir2 = Circle(7, 8, 2)
    Circle.persechenie(cir1, cir2)
    Circle.concentrichnost(cir1, cir2)
    print("Площадь круга:", round(Circle.area(cir1), 2))
    print("Длина окружности:", round(Circle.perimeter(cir1), 2))

