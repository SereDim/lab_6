'''
Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
від 50 до 100.
Серебренніков Дмитро
'''
from random import randint
d=int(input())#заданое число
c=1
e=0
for a in range(10):#диапазон
    b=randint(50,100)#рандом
    if b<d:#условие
        e+=1#чере смотрим есть ли вообще такие числа чтобы не было в конце 1
        c=c*b#сумма
if e==0:
    print(0)
else:
    print(c)
