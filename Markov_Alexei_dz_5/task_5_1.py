# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#  A = 3; B = 5 -> 243 (3⁵)
#  A = 2; B = 3 -> 8

def Degree_of(a, b):
    if b == 0:
        return 1
    return a * Degree_of(a, b - 1)

num_a = int(input("Введите первое число: "))
num_b = int(input("Введите второе число: "))
print(f"A = {num_a}; B = {num_b} -> {Degree_of(num_a, num_b)}")