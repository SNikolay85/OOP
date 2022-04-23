documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Губкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def search_people(doc):
    number_p = input('Введи номер документа: ')
    for human in doc:
        if human['number'] == number_p:
            print(f"Номер документа принадлежит: {human['name']}")
            break
    if human['number'] != number_p:
        print('Нет такого номера')


# Вариант для поиска полки с условием по вхождению
def search_shelf(shelfs):
    number_s = input('Введи номер документа: ')
    for shelf, shelf_contents in shelfs.items():
        if number_s in shelf_contents:
            print(f'Искомый документ на полке №{shelf}')
            return
    print('На полках нет такого документа')

    # Вариант для поиска полки с вложенным циклом


# def search_shelf(shelfs):
#   number_s = input('Введи номер документа: ')
#   for shelf, shelf_contents in shelfs.items():
#     for num_doc in shelf_contents:
#       if num_doc == number_s:
#         print(f'Искомый документ на полке №{shelf}')
#         return
#   print('На полках нет такого документа')

def list_(lst):
    for info in lst:
        print(info['type'], f"'{info['number']}' '{info['name']}'")


def add_(data, shelf):
    type = input('Введи тип документа: ')
    number = input('Введи номер документа: ')
    name = input('Введи имя человека: ')
    num_shelf = input('Введи номер полки: ')
    data.append({'type': type, 'number': number, 'name': name})
    while num_shelf not in shelf.keys():
        print('Такой полки не существует')
        num_shelf = input('Введи номер полки: ')
    else:
        shelf[num_shelf].append(number)


def del_doc(data, shelf):
    while True:
        number = input('Введи номер документа: ')
        for doc in data:
            if doc['number'] == number:
                data.remove(doc)
        for num_shelf, num in shelf.items():
            for n_doc in num:
                if n_doc == number:
                    num.remove(n_doc)
                    return
        print('Нет такого документа')


def move_doc(shelf):
    number_shelf = input('Введи номер целевой полки: ')
    while number_shelf not in shelf.keys():
        print('Такой полки не существует')
        number_shelf = input('Введи номер полки: ')
    else:
        while True:
            number = input('Введи номер документа: ')
            for num_shelf, num in shelf.items():
                for n_doc in num:
                    if n_doc == number:
                        num.remove(n_doc)
                        shelf[number_shelf].append(number)
                        return
            print('Нет такого документа')


def add_shelf(shelf):
    num_shelf = input('Введи номер новой полки: ')
    while num_shelf in shelf.keys():
        print('Такая полка уже существует')
        num_shelf = input('Введи номер новой полки: ')
    else:
        shelf[num_shelf] = []


def view(doc, shelf):
    print(doc)
    print()
    print(shelf)


def secretary(doc, direct):
    message = (f'p - поиск человека по номеру документа \n'
               f's – поиск полки по номеру документа \n'
               f'l – список всех документов \n'
               f'a – добавить новый документ \n'
               f'd – удалить документ из каталога и полок \n'
               f'm – переместить документ на другую полку \n'
               f'as – создать новую полку \n'
               f'q - выход')
    while True:
        print(message)
        comand = input('\nВведи команду: ')
        if comand == 'p':
            print()
            search_people(doc)
            print()
        elif comand == 's':
            print()
            search_shelf(direct)
            print()
        elif comand == 'l':
            print()
            list_(doc)
            print()
        elif comand == 'a':
            print()
            add_(doc, direct)
            print()
        elif comand == 'd':
            print()
            del_doc(doc, direct)
            print()
        elif comand == 'm':
            print()
            move_doc(direct)
            print()
        elif comand == 'as':
            print()
            add_shelf(direct)
            print()
        elif comand == 'v':
            print()
            view(doc, direct)
            print()
        elif comand == 'q':
            break


secretary(documents, directories)