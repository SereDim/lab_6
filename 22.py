'''
Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
Заповнення масиву здійснити випадковими числами від 5 до 500.
Серебренніков Дмитро
'''
from random import randint
c=1
for a in range(10):#диапазон
    b=randint(5,500)#рандом
    if b%3==0 and b>1:#условие, 3 есть подмножеством 9...За диагромой Эйлера-Венна
        c=c*b#хотя с условия не понятно то ли одновременно они должны быть кратными
        #то ли отдельно если отдельно то берутся ли элементы по 2 раза(9 кратно и 9 и 3)
    print(b)
if c==1:
    print(0)
else:
    print(c)
