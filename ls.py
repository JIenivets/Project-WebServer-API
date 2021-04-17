#
# Этот файл отвечает за работу бота в личный сообщениях сообщества.
# Добавление и изменения дз.
#


import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
from vk_api.utils import get_random_id
from keybords_list import *
import save_timetable

vk_session = vk_api.VkApi(token='21637254d5aba72197e3a94f92ef9972e7eab55333562e1220acd7f203574198dad57464e7745e941f529')
lslongpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

running = True
add_mod = False             # Переменная вкл./выкл. режима добавления заданйи
info_mod = False            # Переменная вкл./выкл. режима вывода дополнитеьлной информации о добавлении дз
editSaves_mod = False       # Переменная вкл./выкл. режима редактирования сохранённых заданий
delPredmet_mod = False      # Переменная вкл./выкл. ожидания ввода названия предмета для удаления из сохранений


# Функция для отправки сообщений ботом
def reply_message(text):
    vk.messages.send(
        user_id=event.user_id,
        message=text,
        random_id=get_random_id(),
    )


# Функция для отправки сообщений ботом, но с открытием клавиатур
def reply_message_with_keybords(text, keyboards):
    vk.messages.send(
        user_id=event.user_id,
        message=text,
        random_id=get_random_id(),
        keyboard=keyboards.get_keyboard()
    )


print('Бот ls запушен')

while running:
    # Основной цикл, в котором проверяются и обрабатываются сообщения
    for event in lslongpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.from_user:
            user_message = event.message.lower()
            # Условия для проверки сообщений пользовотелей.
            if add_mod:
                if user_message == '<= назад' and info_mod:
                    reply_message_with_keybords('Ожидание дз, продолжается', keyboard_addTimetable)
                    info_mod = False
                elif user_message == '<= назад' and info_mod is False:
                    add_mod = False
                    info_mod = False
                    reply_message_with_keybords('Ожидание дз, завершено', keyboard_main)
                elif user_message[:-2] == 'более подробная инструкция':
                    reply_message_with_keybords('Добавлять можно, только по одному предмету.\n'
                                                'Необходимо ввести, СТРОГО, предмет и задание, через "*",'
                                                '\nсамо домашнее задание (параграфы, номера и т.п) можно через пробелы'
                                                '\n\n\nПримеры:\n\nалгебра*173 492 583\nАлгЕбРа * параграф 18 '
                                                'номера 800,100\n\nРегистр(заглавные или строчные буквы) не важен, '
                                                'оформление дз - неважно. Главное, чтобы предмет и домашнее задание '
                                                'были разделены "*", в ином случие дз сохранится криво. Так же не'
                                                'забывайте о правильности написания учебных предметов.'
                                                , keyboard_moreInfo)
                    info_mod = True
                else:
                    res = save_timetable.add_dz(user_message)
                    if res is True:
                        reply_message_with_keybords('Задение добавлено', keyboard_main)
                        add_mod = False
                        info_mod = False
                    else:
                        reply_message(res+'❗')
            elif editSaves_mod:
                if delPredmet_mod:
                    if user_message == 'нет':
                        reply_message('Ожидание завершено👌')
                        delPredmet_mod = False
                    else:
                        text = save_timetable.delete_predmet(user_message)
                        reply_message(text)
                        delPredmet_mod = False
                else:
                    if user_message == 'вывести список сохраненных предметов':
                        text = save_timetable.return_predmet_list()
                        reply_message(text)
                    elif user_message == 'удалить предмет':
                        reply_message('Напишите только имя предмета, который ходите удалить или "нет" '
                                      'для завершения ожидания')
                        delPredmet_mod = True
                    elif user_message == '<= назад':
                        reply_message_with_keybords('*куда-то вернулись*', keyboard_main)
                        editSaves_mod = False
            else:
                if user_message in ['@', 'yfxfnm', 'начать']:
                    reply_message_with_keybords('* здесь должно быть краткое описание *', keyboard_main)

                elif user_message == 'добавить домашнее задание':
                    reply_message_with_keybords('Добавлять можно, только по одному предмету.\n'
                                                'Предмет и задание должный быть разделены "*"',
                                                keyboard_addTimetable)

                    add_mod = True

                elif user_message == 'редактировать сохранения':
                    reply_message_with_keybords('Хотите что-то изменить?😉', keyboard_editSaves)
                    editSaves_mod = True
                elif user_message == '<= назад':
                    reply_message_with_keybords('*куда-то вернулись*', keyboard_main)
                else:
                    reply_message_with_keybords('Чтобы добавить дз, нажмите на кнопку "Добавить домашнее задание"',
                                                keyboard_main)


if __name__ == '__main__':
    running = True
