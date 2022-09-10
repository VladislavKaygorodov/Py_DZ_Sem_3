# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Введите преобразуемое число: "))
list = []
temp = number
result = ""
while temp > 0:
    if temp %2 ==0:
        list.insert(0,0)
    elif temp %2 == 1:
        list.insert(0,1)
    temp =int(temp /2)

for i in list:
    result = result + str(i)

print(f"Число {number} в двоичной системе выклядит как {result}")