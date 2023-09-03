# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а 
# некоторые – гербом. Определите минимальное 
# число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и 
# той же стороной. Выведите минимальное количество 
# монет, которые нужно перевернуть

coins = int(input("Введите количество монет: "))
import random
coin_list = [random.randint(0, 1) for _ in range(coins)]
print (*coin_list)
heads = 0
tails = 0

for i in coin_list:
    if i == 0:
        heads += 1
    elif i == 1:
        tails += 1

if tails > heads:
    flips = heads
else:
    flips = tails
    
print("Минимальное количество переворотов:", flips)