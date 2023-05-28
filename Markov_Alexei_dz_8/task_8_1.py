

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
def entered_new_abonent(): #ввод данных нового абонента
    abonent = input("Введите Фамилию, Имя, Отчество, Номер телефона через пробел: ")
    return abonent

def new_abonent(message): # Запись нового абонента в файл
    with open(PATH, 'a+', encoding='UTF-8') as data:
        data.write(f'{message}\n')

def search_in_file(str_zapros): # Здесь ищем нужное
    with open(PATH, 'r', encoding='UTF-8') as data:
        for i in data:
            if str_zapros in i:
                print(i)

def read_file(): # Вывод всех данных из файла построчно
    with open(PATH, 'r', encoding='UTF-8') as data:
        for i in data:
            print(i.strip())

print("*** Программа телефонный справочник ***")
print("Ввести в справочник нового абонента - 1")
print("Найти в справочнике абонента по одному из элементов - 2")
print("Ввывести справочник в консоль построчно - 3")

with open(PATH, 'a', encoding='UTF-8') as data:
    pass
run = True
while run:
    programm_code = int(input("Введите номер необходимой операции со справочником: "))
    corrected_code = [0, 1, 2, 3, 4, 5]
    if programm_code in corrected_code:
        if programm_code == 1:
            new_abonent(entered_new_abonent())
        elif programm_code == 2:
            search_in_file(input('Введите искомое: '))
        elif programm_code == 3:
            read_file()
        elif programm_code == 0:
            run = False
    else:
        print("Введите корректный код!")
print("До свидания!")