"""Задача 3
В ящике имеется 15 деталей, из которых 9 окрашены. 
Рабочий случайным образом извлекает 3 детали. 
Какова вероятность того, что все извлеченные детали окрашены?"""

p1 = 9/15
p2 = 8/14
p3 = 7/13
p = p1 * p2 * p3
print('вероятность того, что все извлеченные детали окрашены: ', round(p, 4))
