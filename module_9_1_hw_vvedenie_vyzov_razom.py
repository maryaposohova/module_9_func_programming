def apply_all_func(int_list, *functions):
    results = {}
    for f in functions:
        results[f.__name__] = f(int_list) #  ключ ф из имени функции, а значение результат функции над списком
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

''' Сылка на задание: 
https://urban-university.ru/members/courses/course999421818026/20231129-0000domasnee-
zadanie-po-teme-vvedenie-v-funkcionalnoe-programmirovanie-263216598740 '''