
__author__ = 'Ловягин Даниил Анатольевич'
# Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.
# TODO: код пишем тут...
user_name = str(input('Введите Ваше Имя:'))
user_age = int(input('Введите Ваш возраст:'))
a = user_age - 18
if user_age > 18:
    print(user_name, 'на', a, 'лет больше 18')
else:
    print(user_name, 'на', abs(a), 'лет меньше 18')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
# TODO: код пишем тут...
a = int(input('Первое число'))
b = int(input('Второе число'))
a = a + b
b = a - b
a = a - b
print('Новое первое число', a)
print('Новое второе число', b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
# TODO: код пишем тут...
from math import *
a = float(input('Введите число а - '))
b = float(input('Введите число b - '))
c = float(input('Введите число c - '))
d = b ** 2 - 4 * a * c #дискриминант
print('Дискриминант =',round(d,2))
if d < 0:
    print('Корней нет')
elif d == 0:
    x = - b / 2 * a
    print('Корень один -',round(x,2))
else:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print('Два корня :','x1=',round(x1,2), 'x1=',round(x2,2))


