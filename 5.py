'''
Створіть масив А [1..7] за допомогою генератора випадкових чисел і
виведіть його на екран. Збільште всі його елементи в 2 рази.
Серебренніков Дмитро
'''
from random import randint
c=list()
for a in range(1,8):#цикл от 1 к 7
    b=randint(1,7)#рандом от 1 к 7
    b=b*2#умножаем на 2
    c.append(b)#переносим в пустой список
print(c)
