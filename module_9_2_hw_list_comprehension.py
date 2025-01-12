def len_str(x):  # длина строк
    return len(x)

def more_equal_5(x): # фильтруем длину строк, больше или равно 5
    # return len_str(x) >= 5
    return len(x) >= 5


# списки
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']


first_result = list(map(len_str, filter(more_equal_5, first_strings)))
print()
# second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
second_result = [(x, y)
                 for x in first_strings
                 for y in second_strings
                 if len_str(x) == len_str(y)]
print()
third_result = {x: len_str(x) for x in first_strings + second_strings if len_str(x) % 2 == 0  }


print(first_result)
print(second_result)
print(third_result)

'''  
Ссылка на задание: 
https://urban-university.ru/members/courses/course999421818026/20231130-0000domasnee-
zadanie-po-teme-spiskovye-slovarnye-sborki-574320194557

'''