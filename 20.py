'''
Знайти суму всіх елементів масиву дійсних чисел, більших за задане
число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
від 50 до 100.
Серебренніков Дмитро
'''
from random import randint
d=int(input())#заданое число
c=0
for a in range(20):#диапазон
    b=randint(50,100)#рандом
    if b>d:#условие
        c=c+b#сумма
print(c)
