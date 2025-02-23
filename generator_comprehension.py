# генераторные сборки
"""
- имеют отличия от списковых и словарных сорок (кортежных сборок нет)
    - записываюся с помощью круглых скобок (и это не кортежные сборки)
    - переменная, содержащая СПИСКОВУЮ сборку хранит в памяти вычисления,
      а ГЕНЕРАТОРНАЯ хранит только саму сборку, а данные нети это наз. ленивыми вычислениями.
      (Каждый элемент в этой сборке, если по нему пройтись циклом фор вычислился и забылся,
      потом слкдующий также..., их нужно отдеьно сохранять. если нужны)

- делают вычисления по мере необходимости
- выполняются только один раз
- занимают мало места в памяти
- работают быстро и эффективно
"""


"""Пример 1"""

# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# result = (x ** 100 for x in my_numbers)
# print(result)

# for elem in result:
#     print(elem)
# print('Еще разок. Второй раз не выведется, потому что генер. сборка вып. только 1 раз')
# for elem in result:
#     print(elem)



"""Пример 2 разница во времени выполнения списковой и генераторной сборки
# # Аписковая сборка: время в милисекундах вышло ~ 10.000726699829102"""
# # #
# import  time
#
# start_time = time.time() # начало программы
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = [x ** 3000 for x in my_numbers]
#
# for i in result:
#     print(i)
#
# finish_time = time.time() # конец программы
# print(f"Время в милисекундах: {(finish_time - start_time) * 1000}")
#
# print()
#
# # Генераторная сборка: время в милисекундах вышло ~ 1.9974708557128906
# import  time
#
# start_time = time.time() # начало программы
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = (x ** 3000 for x in my_numbers)
#
# for i in result:
#     print(i)
#
# finish_time = time.time() # конец программы
# print(f"Время в милисекундах: {(finish_time - start_time) * 1000}")


"""Пример 3
лЛенивые функции используются  в:
-range()
-zip()
-open()
-map()
"""
# пример встроенных функций с ленивыми вычислениями
list_1 = [1, 5, 9, 29, 4]
list_2 = [5, 2, 9, 1, 2]

ran =range(10, 30)
zp = zip(list_1, list_2)
mp = map(str, list_1)

ran1 = list(range(10, 30))
zp1= dict(zip(list_1, list_2))
mp1 = tuple(map(str, list_1))

print(ran, zp, mp) # выведутся как объукты в основном, потому что вычислений не было еще
print()
print(ran1, zp1, mp1) # выведутся результаты
print()

#
# # при передаче в лист вычисления приизойдут и мы их увидим в выводе
# print(list(ran))
print(list(zp))
# print(list(mp))

#можно сохранить в переменные
# a , b, c= list(ran), list(zp), list(mp)
# print(a)
# print(b)
# print(c)
print()

st = set(list_1 + list_2)
print(st)