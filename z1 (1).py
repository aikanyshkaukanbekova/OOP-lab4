#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    a = input("Введите первое значение: ")
    b = input("Введите второе значение: ")

    if a.isnumeric() and b.isnumeric():
        a = int(a)
        b = int(b)

    print(a + b)
