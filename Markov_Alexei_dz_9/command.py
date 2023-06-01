import text
import model
import view

def start():
    print(text.main_menu)
    run = True

    while run:
        command = input("Введите номер необходимой операции со справочником: ")
        if command.isdigit() and 0 <= int(command) <= 5:
            command = int(command)
            if command == 1:
                model.create_new_user(view.entered_new_user())
            elif command == 2:
                model.search_in_file(view.searching_used())
            elif command == 3:
                model.read_file()
            elif command == 4:
                model.replace_in_file(view.searching_used())
            elif command == 5:
                model.del_in_file(view.searching_used())
            elif command == 0:
                run = False
        else:
            print("Введите корректный код!")

    print("До свидания!")