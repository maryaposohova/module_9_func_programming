
# 1 Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x[0] == y[0], first, second))
print(result)


# 1 Замыкание
# просто запись в файл
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for d in data_set:
                file.write(f'{d}\n')

    return write_everything

# # запись в файл, чтение и вывод на печать
# def get_advanced_writer(file_name):
#     def write_everything(*data_set):
#         with open(file_name, 'w', encoding='utf-8') as file:
#             for d in data_set:
#                 file.write(f'{d}\n')
#         with open(file_name, 'r', encoding='utf-8') as file:
#             for _ in data_set:
#                 print(file.read())
#     return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# 3 Метод __call__
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())



"""Ссылка на задание:
https://urban-university.ru/members/courses/course999421818026/20231202-
0000domasnee-zadanie-po-teme-sozdanie-funkcij-na-letu-315311639613
"""
