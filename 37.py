'''
Розсортуйте заданий лінійний масив по зростанню.
Серебренніков Дмитро
'''
a=[345,546,456,65,56,657,5664]
for b in range(len(a)-1):#selection sort
    c=b#минимальный элемент находим
    for d in range(b+1,len(a)):#и ставим его в конец
        if a[d]<a[c]:#и так по порядку самые меньшие с оставшиъся выставляем
            c=d#по порядку
        a[b],a[c]=a[c],a[b]#
print(a)
