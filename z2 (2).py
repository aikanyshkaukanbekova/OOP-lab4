#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import random

if __name__ == '__main__':
    try:
        n = int(input("Введите высоту матрицы: "))
        m = int(input("Введите ширину матрицы: "))
        a = int(input("Введите левый диапазон чисел: "))
        b = int(input("Введите правый диапазон чисел: "))
    except Exception as e:
        print("Ошибка: Необходимо ввести числа")
        exit(1)

    matrix = []

    for i in range(0, n):
        r = []
        for j in range(0, m):
            r.append(random.randint(a, b))
        matrix.append(r)

    print(matrix)
