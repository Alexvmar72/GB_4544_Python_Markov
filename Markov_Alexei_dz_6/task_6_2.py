# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
min_value = int(input("Введите минимальное значение диапазона: "))
max_value = int(input("Введите максимальное значение диапазона: "))
my_list = [random.randint(1, 20) for _ in range(20)]
print(my_list)
for i in range(len(my_list)):
    if min_value <= my_list[i] <= max_value:
        print(i)