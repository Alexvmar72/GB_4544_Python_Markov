

# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# . Добавить контакт
# . Найти контакт
# . Выход

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных

PATH = 'phonebook.txt'
def entered_new_user(): #ввод данных нового абонента
    user = input("Введите Фамилию, Имя, Отчество, Номер телефона через пробел: ")
    return user

def create_new_user(message): # Запись нового абонента в файл
    with open(PATH, 'a+', encoding='UTF-8') as data:
        data.write(f'{message}\n')

def search_in_file(str_finding): # Здесь ищем нужное
    with open(PATH, 'r', encoding='UTF-8') as data:
        for row in data:
            if str_finding in row:
                print(row)
        else:
            print("Нет такого контакта")

def replace_in_file(str_finding): # Здесь ищем нужное и меняем
    with open(PATH, 'r+', encoding='UTF-8') as data:
        for row in data:
            if str_finding in row:
                data.write(input("Введите новые Фамилию, Имя, Отчество, Номер телефона через пробел: "))
            # Тут что-то пока не получается. Дописывает, но не меняет.


def read_file(): # Вывод всех данных из файла построчно
    with open(PATH, 'r', encoding='UTF-8') as data:
        print()
        print(data.read())
        print()

print("*** Программа телефонный справочник ***")
print("Ввести в справочник нового абонента - 1")
print("Найти в справочнике абонента по одному из элементов - 2")
print("Ввывести справочник в консоль построчно - 3")
print("Внести изменения в записи в справочнике - 4")

with open(PATH, 'a', encoding='UTF-8') as data:
    pass
run = True
while run:
    command = int(input("Введите номер необходимой операции со справочником: "))
    corrected_code = [0, 1, 2, 3, 4, 5]
    if command in corrected_code:
        if command == 1:
            create_new_user(entered_new_user())
        elif command == 2:
            search_in_file(input('Введите искомое: '))
        elif command == 3:
            read_file()
        elif command == 4:
            replace_in_file(input('Введите искомое: '))
        elif command == 0:
            run = False
    else:
        print("Введите корректный код!")
print("До свидания!")