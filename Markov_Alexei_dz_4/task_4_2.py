# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора
# на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
#
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

number_bushes = int(input("Введите количество кустов: "))
lst_bushes_berry = []
for i in range(number_bushes):
    number_berry = int(input(f"Введите количество ягод на {i+1} кусте: "))
    lst_bushes_berry.append(number_berry)
number_berry = 0
lst_bushes_berry += lst_bushes_berry[:2]
for i in range(number_bushes):
    number_berry = max(number_berry, lst_bushes_berry[i] + lst_bushes_berry[i + 1] + lst_bushes_berry[i + 2])
print(f"Максимальное число ягод: {number_berry}")


