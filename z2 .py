#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import random

class Matrix:
    def __init__(self, n, m, a, b):
        """
        n - Ширина матрицы
        m - Высота матрицы
        a и b - Диапазоны случайных чисел для матрицы
        """
        self._matrix = []

        for i in range(0, n):
            r = []
            for j in range(0, m):
                r.append(random.randint(a, b))
            self._matrix.append(r)

    def __str__(self):
        return str(self._matrix)

if __name__ == '__main__':
    try:
        n = int(input("Введите высоту матрицы: "))
        m = int(input("Введите ширину матрицы: "))
        a = int(input("Введите левый диапазон чисел: "))
        b = int(input("Введите правый диапазон чисел: "))
    except Exception as e:
        print("Ошибка: Необходимо ввести числа")
        exit(1)

    matrix = Matrix(n, m, a, b)

    print(matrix)
