# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

size = int(input("Введите размер списка: "))
list = []
while len(list) != size:
    list.append(random.randint(0,size))
print(list)

i=0
result =0
while i != len(list):
    if i % 2 ==1:
        result += list[i]
    i +=1

print(f"результат суммы нечетных чисел в списке является: {result}")