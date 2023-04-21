# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


first_array_count = int(input("Введите количество элементов первого множества: "))
second_array_count = int(input("Введите количество элементов второго множества: "))

set_first_array = set(int(input(f"Введите {first_array_count} элементов первого множества")) for _ in range(first_array_count))
set_second_array = set(int(input(f"Введите {second_array_count} элементов второго множества")) for _ in range(second_array_count))
result = sorted(set_first_array.intersection(set_second_array))
print(set_first_array)
print(set_second_array)
print(result)