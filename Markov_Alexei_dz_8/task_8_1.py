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
    print(f'Введён новый абонент: {user}')
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
    with open(PATH, "r", encoding='UTF-8') as file:
        lines = file.readlines()
        count = 0
        for i in range(len(lines)):
            if str_finding in lines[i]:
                lines[i] = input("Введите новые Фамилию, Имя, Отчество, Номер телефона через пробел: ")

    with open(PATH, "w", encoding='UTF-8') as file:
        file.writelines(lines)

def read_file(): # Вывод всех данных из файла построчно
    with open(PATH, 'r', encoding='UTF-8') as data:
        print()
        print(data.read())
        print()

def del_in_file(str_finding): # Удаление данных из файла
    with open(PATH, "r", encoding='UTF-8') as file:
        lines = file.readlines()
        count = len(lines)
        for i in range(count):
            if i < count and str_finding in lines[i]:
                print(f'Найденная строка: {lines[i]}')
                switch_choice = input('Удаляем? Если "да" нажмите "д", если нет, любую другую клавишу: ')
                if switch_choice == 'д':
                    print(f'Строка: {lines[i]} удалена')
                    del lines[i]
                    count = count - 1
        else:
            print('Такого значения для удаления нет')

    with open(PATH, "w", encoding='UTF-8') as file:
        file.writelines(lines)

main_menu = """*** Программа телефонный справочник ***
1 - Ввести в справочник нового абонента
2 - Найти в справочнике абонента по одному из элементов
3 - Вывод справочника в консоль построчно
4 - Внести изменения в записи в справочнике
5 - Удалить запись в справочнике
0 - Выйти из программы
"""

print(main_menu)
run = True

while run:
    command = input("Введите номер необходимой операции со справочником: ")
    if command.isdigit() and 0 <= int(command) <= 5:
        command = int(command)
        if command == 1:
            create_new_user(entered_new_user())
        elif command == 2:
            search_in_file(input('Введите искомое: '))
        elif command == 3:
            read_file()
        elif command == 4:
            replace_in_file(input('Введите искомое: '))
        elif command == 5:
            del_in_file(input('Введите искомое: '))
        elif command == 0:
            run = False
    else:
        print("Введите корректный код!")

print("До свидания!")