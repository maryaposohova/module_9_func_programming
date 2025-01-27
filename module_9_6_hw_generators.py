def all_variants(text):  # generator
    l = len(text)
    for size in range(1, l + 1):  # с 1 и до длины +1
        for start in range(l - size + 1):  # начало
            yield text[start:start + size]

a = all_variants("abc")
for i in a:
    print(i)

"""
Ссылка на задание:
https://urban-university.ru/members/courses/course999421818026/20231204-
0000domasnee-zadanie-po-teme-generatory-155372347511
"""