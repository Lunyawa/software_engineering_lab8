#!/usr/bin/env python3
# -*- coding: utf -8 -*-

if __name__ == '__main__':
    # Ввести кортеж одной строчкой
    a = tuple(map(int, input("Введите кортеж: ").split()))
    b = ()

    b_l = list(b)

    # Составление нового кортежа по правилу задачи
    for i, item in enumerate(a):
        if (i + 1) % 2 == 0:
            b_l.append(item ** 2)
        else:
            b_l.append(item * 2)

    b = tuple(b_l)
    print(f'a = {a} \nb = {b}')
