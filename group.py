#
# Этот файл отвечает за работу бота в беседах.
# Получение команд и вывод ответа на них
#

import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import save_timetable


vk_session = vk_api.VkApi(token='21637254d5aba72197e3a94f92ef9972e7eab55333562e1220acd7f203574198dad57464e7745e941f529')
longpoll = VkBotLongPoll(vk_session, group_id=200818735)
vk = vk_session.get_api()


# Функция для отправки сообщений ботом
def reply_message(text):
    vk.messages.send(
        chat_id=event.chat_id,
        message=text,
        random_id=get_random_id(),
    )


print('Бот group запушен')

# Основной цикл, в котором проверяются и обрабатываются сообщения
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
        users_message = event.message.get('text').lower()
        # Условия для проверки сообщений пользовотелей.
        if users_message == '!дз':
            text = 'Текущее:\n\n'
            text += save_timetable.return_dz('new')
            reply_message(text)
        elif users_message == '!дз прошлое':
            text = 'Прошлое:\n\n'
            text += save_timetable.return_dz('before')
            reply_message(text)
        elif users_message == '!дз команды':
            reply_message('Команды Бота:\n\n"!дз" - выводит актуальное домашнее задание;\n"!дз прошлое" - '
                          'задание, которое было до актуального, если же его нет, пишется "сохранения нет🤷‍♂‍";\n'
                          '"!дз команды" - список команд Бота с их описанием;')
        else:
            print('Введена неизвестная команда')
