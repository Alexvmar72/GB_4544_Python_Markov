# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов
# в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

size_array_n = int(input("Введите размер массива: "))
search_number_x = int(input("Введите заданное число: "))
array_lst = list(range(1, size_array_n+1))
result_number = array_lst[0]
temp_difference = 0
temp_difference_min = search_number_x - array_lst[0]
i = 1
while i < len(array_lst):
    temp_difference = search_number_x - array_lst[i]
    if abs(temp_difference) < abs(temp_difference_min):
        temp_difference_min = temp_difference
        result_number = array_lst[i]
    i += 1


print(array_lst)
print(search_number_x)
print(f"Самый близкий по величине элемент {result_number}")