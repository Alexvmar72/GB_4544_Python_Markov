def searching_used():
    search = input('Введите искомое: ')
    return search

def entered_new_user(): #ввод данных нового абонента
    user = input("Введите Фамилию, Имя, Отчество, Номер телефона через пробел: ")
    print(f'Введён новый абонент: {user}')
    return user