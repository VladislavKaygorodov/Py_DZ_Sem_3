# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
number = int(input("Введите преобразуемое число: "))
list = [0]
num = number

if num < 0:
    num *=-1

temp = 1

while temp <= num:
    list.append(fibonacci(temp))
    temp +=1

temp_list = []
for i in range(0, len(list)):
    temp_list.append(list[i])
temp_list.pop(0)
for i in range(1, len(list)-1, 2):
  temp_list[i] *= -1
k=0
size = len(list) + len(temp_list)
while len(list) < size:
    list.insert(0, temp_list[k])
    k+=1
print(list)
