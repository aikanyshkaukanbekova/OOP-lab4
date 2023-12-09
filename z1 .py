#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

class Box:
    """
    Класс для хранения введенного значения
    """
    def __init__(self, x: str):
        self.x = x

    def __add__(self, other):
        """
        Если оба x - это числа, то суммируем их, иначе конкатенируем строки
        """
        x = self.x
        y = other.x

        if x.isnumeric() and y.isnumeric():
            x = int(x)
            y = int(y)

        self.x = x + y

        return self.x

    def __str__(self):
        return str(self.x)

if __name__ == '__main__':
    a = Box(input("Введите первое значение: "))
    b = Box(input("Введите второе значение: "))

    print(a + b)
