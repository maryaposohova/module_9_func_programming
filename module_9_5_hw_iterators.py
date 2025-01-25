
class StepValueError(ValueError):
    pass

class Iterator:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step > 0:  # шаг +
            if self.pointer > self.stop:
                raise StopIteration()
        else:               # шаг -
            if self.pointer < self.stop:
                raise StopIteration()
        value = self.pointer # сохраняем значение и затем к поинтеру добавляем шаг
        self.pointer += self.step
        return value



try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()


"""Ссылка на задание:
https://urban-university.ru/members/courses/course999421818026/20231203-
0000domasnee-zadanie-po-teme-iteratory-699145666000
"""