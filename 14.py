'''
Сформуйте лінійний масив дійсних чисел, елементи якого є відстанями,
пройденими тілом при вільному падінні на землю за 1, 2, ..., 10 с.
Серебренніков Дмитро
'''
#Ничего не понял
a=int(input())
d=list()
for b in range(1,11):#диапазон времени
    c=b*a#Если тело движется равномерно, то каждый элемент массива это растояние котторое он проешл за определенное время
    d.append(c)#добавляем элемент в массив
print(d)#
