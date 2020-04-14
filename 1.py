'''Реалізувати програму, в якій кожен з алгоритмів сортування оформити як окрему
функцію. Проілюструвати механізм використання параметрів різних типів. Забезпечити
підрахунок числа необхідних порівнянь, числа обмінів і часу роботи кожної функції,
сформувавши функції оцінки ефективності методів сортування. Підготувати єдині для
всіх алгоритмів тестові вихідні дані:

• згенерована послідовність псевдовипадкових чисел, достатня для оцінки
швидкості роботи алгоритму сортування (близько 100000 цілих чисел);

• вихідна послідовність псевдовипадкових чисел, відсортована будь-яким методом
в порядку зростання;

• вихідна послідовність псевдовипадкових чисел, відсортована будь-яким методом
в порядку за спаданням;

• забезпечити програмну можливість вибору введення вихідних даних з клавіатури
до 30 вихідних чисел.
Для програми привести лістинг з результати роботи:

• вихідний масив (вивести на екран для випадку введення вихідних даних з
клавіатури);

• відсортований масив (для випадку введення вихідних даних з клавіатури один
екземпляр відсортованого масиву вивести на екран);

• показники функції оцінки ефективності методів сортування (вивести на екран).

Виконати сортування масиву цілих чисел
в порядку зростання / за спаданням елементів.
Найпростіші алгоритми сортування:
• сортування бульбашкою (bubble sort);
• сортування вибором (selection sort);
• сортування вставками (insertion sort). 

Серебренніков Дмитро Олександрович
'''
#Импорт модуля для рандома:
import random



from timeit import default_timer as timer#модуль для записи времени





o=input('введите + если хотите ввести значения с калвиатуры или - если автоматически')
i=list()
#Функция без аргументов птч их нет, и работает при вызове:
def d():
    for a in range(1000):
        #В пустой список созданый ранее добавляем все:
        #итерируемые рандомные числа:
        i.append(random.randint(0,100))
if o=='-':#За выбором делает рандомный список
    #Воспроизведение функции:
    d()
elif o=='+':#Или с клавиатуры
    for p in range(30):
        i.append(input('шота'))
else:
    print('RETARD')
    del(i)
#Не сортированный список
print(i)








ae=input('Введите + если хотите чтобы было от меньшего к большему, и - в обратном направлении')
q=input('Введите 1 - bubble, 2 - selection  3  - insertion')










def j(k):#bubble sort
    m=0
    n=True#
    while n:#
        n=False#флаг который если не стал трушным останавливает работу программы птч все отсортировано
        for l in range(len(k)-m-1):#от 0 до размера -1 за условием ренджа и еще -1 птч мы проверяем итерируемый со следующим а не с прошлым
            if k[l]>k[l+1]:#проверяем итерируемый со следующим
                k[l],k[l+1]=k[l+1],k[l]#если больше то меняет местами
                n=True#и если со всех оказалось что были изменения значит еще не все отсортировала программа
        m+=1#значение которое отнимается от каждого последующего прохождения
#selection sort
def r(s):#
    for t in range(len(s)-1):##от 0 до размера -1 за условием ренджа и еще -1 птч последний эелемент будет уже отсорт.
        u=t#минимальное значение которое равно номеру итерации
        for v in range(t+1,len(s)):#элементы с коротыми мы будет сравнивать выбраный элемент
            if s[v]<s[u]:#если выбраный меньше чем итерируемый то это в обратном направлении
                u=v#выбраный элемент становится равным итерируемому
        s[t],s[u]=s[u],s[t]#и меняет их местами

#insertion sort
def w(arrayToSort):#функция
    a = arrayToSort#быстрая замена
    for i in range(len(a)):#диапазон
        v = a[i]#быстрая замена за индексом
        j = i#приравниваем значения
        while (a[j-1] > v) and (j > 0):#пока значения с индексом  j-1 больше числа за индексом по итерации и оно больше 0
            a[j] = a[j-1]#уменьшаем двигемся влево
            j = j - 1#уменьшаем значение
        a[j] = v#приравниваем обратно когда выходим с цыкла
    return a#возвращаем отсортированный список

def af(k):#bubble sort в обратном направлении
    m=0
    n=True#
    while n:#
        n=False#флаг который если не стал трушным останавливает работу программы птч все отсортировано
        for l in range(len(k)-m-1):#от 0 до размера -1 за условием ренджа и еще -1 птч мы проверяем итерируемый со следующим а не с прошлым
            if k[l]<k[l+1]:#проверяем итерируемый со следующим
                k[l],k[l+1]=k[l+1],k[l]#если больше то меняет местами
                n=True#и если со всех оказалось что были изменения значит еще не все отсортировала программа
        m+=1#значение которое отнимается от каждого последующего прохождения



#selection sort в обратном направлении
def ag(s):#
    for t in range(len(s)-1):##от 0 до размера -1 за условием ренджа и еще -1 птч последний эелемент будет уже отсорт.
        u=t#минимальное значение которое равно номеру итерации
        for v in range(t+1,len(s)):#элементы с коротыми мы будет сравнивать выбраный элемент
            if s[v]<s[u]:#если выбраный меньше чем итерируемый то это в обратном направлении
                u=v#выбраный элемент становится равным итерируемому
        s[t],s[u]=s[u],s[t]#и меняет их местами


#insertion sort в обратном направлении
def ah(arrayToSort):
    a = arrayToSort
    for i in range(len(a)):
        v = a[i]
        j = i
        while (a[j-1] < v) and (j > 0):
            a[j] = a[j-1]
            j = j - 1
        a[j] = v
    return a










#function=a
#items=b
#elapsed=c
#
#
#
def ai(a):#Функция для записи время
  
    t = timer()#таймер
    a(i)#делаем так чтобы наш аргумент имел свой аргумерт
    c = timer() - t#само время

    print(f'{c} секунд')#вывод






    
if ae=='+':
    if q=='1':
        j(i)#в функцию записываем вместо временного аргумента наше значение, тоесть введенный список
        ai(j)#вызываем функцию записующую время
    elif q=='2':
        r(i)
        ai(r)
    else:#
        w(i)
        ai(w)





if ae=='-':
    if q=='1':
        af(i)#в функцию записываем вместо временного аргумента наше значение, тоесть введенный список
        ai(af)
    elif q=='2':
        ag(i)#
        ai(ag)
    else:#
        ah(i)#
        ai(ah)
print(i)

















