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

