import math

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return "Circle: \t x: {} \t y: {} \t radius: {}".format(self.x, self.y, self.r)

    def area(self):
        return round(math.pi * (self.r ** 2), 2)  # площадь окружности

    def perimeter(self):
        return round(2 * math.pi * self.r,2)  # периметр окружности

    def concentrichnost(self, cir):  # концентричность окружностей
        return self.x == cir.x & self.y == cir.y

if __name__ == '__main__':
    c1 = Circle(3, 5, 3)
    c2 = Circle(7, 8, 2)
    print("Площадь круга:", round(Circle.area(c1), 2))
    print("Длина окружности:", round(Circle.perimeter(c1), 2))
    print("c1 концентричен c2", c1.concentrichnost(c2))

