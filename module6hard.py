from turtle import color
from math import pi, sqrt
class Figure:

    sides_count = 0

    def __init__(self, color: list, *sides: int, filled: bool = None):
        self.__sides = (sides)
        self.__color = (color)
        self.filed = (filled)

    def get_color(self):
        return [*self.__color]

    def __is_vaild_color(self, r, g, b):
        if 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255:
            return r, g, b
        else:
            return False
    def set_color(self, r, g, b):
        if self.__is_vaild_color(r, g, b):
            self.__color = (r, g, b)
    def __is_vaid_sides(self, *new_sides):
        for i in new_sides:
            if len(i) > 0 and len(new_sides) == len(self.__sides):
                return True
            else:
                return False
    def get_sides(self):
        return [*self.__sides]

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_vaid_sides(new_sides):
            self.__sides = new_sides

class Circle(Figure):
    sides_count = 1
    def __radius(self):
        return self.__len__/(2*pi)

    def get_square(self):
        return pi *(self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p =(1/2)*(self.__sides[0] + self.__sides[1] + self.__sides[2])
        return sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list, *sides: int, filled: bool = None):
        super().__init__(color, *sides)
        self.set_sides(*sides * self.sides_count)

    def get_volume(self):
        return self.get_sides()[0]**3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())




