#!/usr/bin/env python3
# -*- coding: utf -8 -*-

if __name__ == '__main__':
    # Ввести кортеж одной строчкой
    a = tuple(map(int, input("Введите кортеж: ").split()))

    b = tuple([item ** 2 if (i + 1) % 2 == 0 else item * 2 for i, item in enumerate(a)])

    print(f'a = {a} \nb = {b}')
