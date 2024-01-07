from csv import DictReader, DictWriter
from os.path import exists

class LenNumberError:
    def __init__(self, txt):
        self.txt = txt
def get_info():
    first_name = 'Ivan'
    last_name = 'Ivanov'
    is_valid_number = False
    while not is_valid_number:
        try:
            phone_number = int(input("Введите номер телефона: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError('Невалидная длина')
            is_valid_number = True
        except ValueError:
            print('Невалидный номер')
            continue
        except LenNumberError as err:
            print(err)
            continue
    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['имя','фамилия','телефон'])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def write_file(file_name):
    res = read_file(file_name)
    user_data = get_info()
    for el in res:
        if el['телефон'] == str(user_data[2]):
            print('Такой пользователь уже существует')
            return
    obj = {'имя': user_data[0],'фамилия': user_data[1],'телефон': user_data[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def copy_line(file_name, obj):
    if not bool(file_name.strip()):
        file_name = f"phone_{obj['телефон']}.csv"
    else:
        file_name += ".csv"
    if not exists(file_name):
        create_file(file_name)
    res = read_file(file_name)
    for el in res:
        if el['телефон'] == str(obj['телефон']):
            print('Такой пользователь уже существует')
            return
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

file_name = 'phone.csv'

def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            read_file_name = input("Введите имя файла: ")
            if not bool(read_file_name.strip()):
                read_file_name = file_name
            else:
                read_file_name += ".csv"
            if not exists(read_file_name):
                print('Файл не создан!')
                continue
            print(*read_file(read_file_name))
        elif command == 'c':
            if not exists(file_name):
                print('Файл не создан!')
                continue
            try:
                number_row = int(input('Введите номер строки для копирования: '))
            except ValueError:
                print('Введено не число!')
                continue

            phone_book = read_file(file_name)
            number_line = len(phone_book)
            if number_row <= 0 or number_row > number_line:
                print('Неверный номер строки!')
                continue

            row = phone_book[number_row - 1]
            new_file_name = input('Введите название файла: ')
            copy_line(new_file_name, row)


main()