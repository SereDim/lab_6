'''
Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в
один рядок через кому. Отримайте для масиву середнє арифметичне.
Серебренніков Дмитро
'''
c=0
d=list()#пустой список который будет выступать строкой
for a in range(5):#через цикл добавляем в список каждый элемент
    b=int(input())
    c=c+b#все числа которые сумируются благодаря рекурсии
    d.append(b)#функция добавления
print(d)
print(c/5)#деление всех чисел
