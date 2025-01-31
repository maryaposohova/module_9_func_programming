# Пример создания простого декоратора

def null_decorator(func):
    return func

def greet():
    return "Hello"

greet = null_decorator(greet)  # переопределили

print(greet())

# Синтаксический сахар, это мы делаем только, если не хотим сохранить функционал основной функции.
# Теперь она всегда будет работать только в связке с декоратором, в отличии от первого варианта.

def null_decorator(func):
    return func

@null_decorator
def greet():
    return "Hello"

print(greet())

# Внутри декоратора мы можем определить еще одну функцию
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
def greet():
    return "Hello"

print(greet())

# Если функциона грит надо оставить:
greet_dec = uppercase(greet)
print(greet_dec())

#
import time
import sys

def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()

        elapses = round(ended_at - started_at, 4)
        print(f'Функция работала {elapses} секунды')
        return result
    return surrogate

@time_track
def digits(*args):
    total = 1
    for number in args:
        total *=  number ** 5000
        return len(str(total))  # эта ф возвращает длину строчки

# sys.set_int_max_str_digits(100000) # увеличиваем максимал длину строчки

result = digits(3141, 5926, 2718, 2818)
print(result)