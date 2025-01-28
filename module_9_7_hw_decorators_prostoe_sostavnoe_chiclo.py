#
# def is_prime(func):
#     def wrapper(*args, **kwargs):
#         result_1 = func(*args, **kwargs)
#         for i in range(2, result_1+1):
#             try:
#                 if result_1 % i == 0:
#                     print("Составное")
#                 else:
#                     print("Простое")
#             except ZeroDivisionError:
#                 print("На ноль делить нельзя")
#             print(result_1, i)
#     return wrapper

def is_prime(func):
    def wrapper(*args, **kwargs):
        result_1 = func(*args, **kwargs)
        isprime = True
        for i in range(2, result_1):
            try:
                if result_1 % i == 0:
                    isprime = False
            except ZeroDivisionError:
                print("На ноль делить нельзя")
            if isprime:  # это тру, число простое
                return f'{result_1} - простое число'
            else:
                return f'{result_1} - составное число'
    return wrapper

@is_prime
def sum_three(*n): #  высчисление суммы
    a = 0
    for i in n:
        a += i
    return a


result = sum_three(2, 3, 6)
print(result)

"""
Ссылка на задание:
https://urban-university.ru/members/courses/course999421818026/20231205-
0000domasnee-zadanie-po-teme-dekoratory-231730783138
"""