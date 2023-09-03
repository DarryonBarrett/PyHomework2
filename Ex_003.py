# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2**k), не превосходящие числа N.

N = int(input("Введите число N: "))

power = 1
result = []

while power <= N:
    result.append(power)
    power *= 2

print("Целые степени двойки, не превосходящие", N, ":")
number = 0
for powers in result:
    print(f'2^{number} =', powers)
    number += 1