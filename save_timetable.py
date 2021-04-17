#
# Файл для работы с json файлом и парсинга сохранений из/в него
#

import json
from pprint import pprint

db = None           # Переменная в которую записывается json файл
predmet = None      # Переменная предмета
zadanie = None      # Переменная задания


# Функция для открытия json файла и записи его в db
def db_open():
    global db
    with open('timetables.json') as f:
        db = json.load(f)


# Функция для открытия json файла и записи db в его
def db_close():
    global db
    with open('timetables.json', 'w') as file:
        json.dump(db, file)


# Функция добавления дз
def add_dz(user_message):
    global db, predmet, zadanie
    db_open()
    if '*' in user_message:
        predmet = user_message[:user_message.find('*')].strip()
        zadanie = user_message[user_message.find('*') + 1:].strip()
        if predmet not in db:
            db[predmet] = {}
            db[predmet]['new'] = zadanie
        else:
            db[predmet]['before'] = db[predmet]['new']
            db[predmet]['new'] = zadanie
        pprint(db)
        db_close()
        return True
    else:
        return 'Неверный формат ввода'


# Функция вывода дз
def return_dz(param):
    global db
    db_open()
    da = ''
    for el in db:
        try:
            da += '\n' + el + ' ' + db[el][param]
        except KeyError:
            da += '\n' + el + ' сохранения нет🤷‍♂'
    return da


# Функция вывода списка предметов
def return_predmet_list():
    global db
    db_open()
    da = ''
    for el in db:
        da += '\n' + el
    return da


# Функция удаления предмета из json
def delete_predmet(user_message):
    global db
    db_open()
    if user_message in db:
        del db[user_message]
        db_close()
        return 'Элемент удалён✅'
    else:
        return 'Этого элемента нет в системе'

