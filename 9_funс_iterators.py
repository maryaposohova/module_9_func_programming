
"""Итераторы"""
import sys
from itertools import repeat

# итераторы экономят память
# Репит - ленивые вычисления, напечатает repeat('4', 100000), тк вычисления еще не прозводились
ex_iterator = repeat('4', 100_000)  # вычисления еще не производятся
print(ex_iterator)  # repeat('4', 100000)
print(f'Размер итераторов {sys.getsizeof(ex_iterator)}')  # Размер итераторов 48

# вычислили
ex_str = '4' * 100_000
print(f'Размер списка {sys.getsizeof(ex_str)}')  # Размер списка 100041

print(sys.getsizeof(ex_str) / sys.getsizeof(ex_iterator))  # разница в 2084.1875 раз


class Iter:
    def __init__(self):
        self.first = 'Первый элемент'
        self.second = "Второй элемент"
        self.third = "Третий элемент"
        self.i = 0

    def __iter__(self):
        # Обнуляем счетчик перед циклом
        self.i = 0
        # Возвращаем себя, так как объект должен быть итератором
        return self

    def __next__(self):
        # тот метод возвращает значения по требованиям пайтон (ленивые вычисления)
        self.i += 1
        if self.i == 1:
            return self.first
        if self.i == 2:
            return self.second
        if self.i == 3:
            return self.third
        if self.i == 4:
            return "Подсчет закончен"
        raise StopIteration()  # Больше возвращать нечего


obj = Iter()
# print(obj)

#  for

# for value in obj:
#     print(value)
#
# # Итератор вызывает метод некст при каждом проходе цикла
# # Если в некст возникает исключение СтопИтерейшн, значит больше нет элементов и цикл прекращается

#  while
try:
    while True:
        value = obj.__next__()
        print(value)
except StopIteration:
    pass


"""fibonacci"""
def fibonacci(n):
    rezult = []
    a, b = 0, 1
    for _ in range(n):
        rezult.append(a)
        a, b = b, a+ b
    return rezult

for value in fibonacci(n=10):
    print(value)

"""Итератор последовательности fibonacci до N юлементов"""
class fibonacci:
    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0, 0, 1, n   # i - это счетчик

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a


fib_iterator = fibonacci(20)
print(fib_iterator)
for value in fib_iterator:
    print(value)
