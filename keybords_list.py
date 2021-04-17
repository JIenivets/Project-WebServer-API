#
# В этом файле объявляются клавиатуры и их кнопки
#

from vk_api.keyboard import VkKeyboard, VkKeyboardColor


# Галавная клавиатура
keyboard_main = VkKeyboard()
keyboard_main.add_button('Добавить домашнее задание', color=VkKeyboardColor.DEFAULT)
keyboard_main.add_line()
keyboard_main.add_button('Редактировать сохранения', color=VkKeyboardColor.DEFAULT)


# Клавиатура режима добавления заданйи
keyboard_addTimetable = VkKeyboard()
keyboard_addTimetable.add_button('Более подробная инструкция ℹ', color=VkKeyboardColor.DEFAULT)
keyboard_addTimetable.add_line()
keyboard_addTimetable.add_button('<= Назад', color=VkKeyboardColor.NEGATIVE)


# Клавиатура для вывода дополнитеьлной информации о добавлении дз
keyboard_moreInfo = VkKeyboard()
keyboard_moreInfo.add_button('<= Назад', color=VkKeyboardColor.NEGATIVE)


# Клавиатура режима редактирования сохранённых заданий
keyboard_editSaves = VkKeyboard()
keyboard_editSaves.add_button('Вывести список сохраненных предметов', color=VkKeyboardColor.DEFAULT)
keyboard_editSaves.add_line()
keyboard_editSaves.add_button('Удалить предмет', color=VkKeyboardColor.DEFAULT)
keyboard_editSaves.add_line()
keyboard_editSaves.add_button('<= Назад', color=VkKeyboardColor.NEGATIVE)
