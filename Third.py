# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

size = int(input("Введите размер списка: "))
list = []
while len(list) != size:
    list.append(round(random.uniform(0,size), 2))
print(list)

list_2 = []

for i in list:
    list_2.append(((i*100) % 100)/100)

max = list_2[0]
min = list_2[0]

for i in list_2:
    if i > max:
        max = i
    if i < min:
        min = i

result =round(max - min, 2)
print(f"Разница максимальной и минимальной дробной части из указанного списка составляет: {result}")