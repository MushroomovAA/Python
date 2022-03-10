list1 = [99, 48, 99.99, 45.5, 0.48, 10, 24, 13.50, 14, 5, 64, 39.90]
list3 = []
for list2 in list1:
    rub = int(list2)
    kop = (list2 - rub) * 100
    list3.append(f'{rub:02} руб. {kop:02.0f} коп.')
list4 = ', '.join(list3)
print(list4)



list1 = [99, 48, 99.99, 45.5, 0.48, 10, 24, 13.50, 14, 5, 64, 39.90]
print(id(list1))
list1.sort()
print(id(list1))
list3 = []
for list2 in list1:
    rub = int(list2)
    kop = (list2 - rub) * 100
    list3.append(f'{rub:02} руб. {kop:02.0f} коп.')
list4 = ', '.join(list3)
print(list4)



list1 = [99, 48, 99.99, 45.5, 0.48, 10, 24, 13.50, 14, 5, 64, 39.90]

list3 = []
for list2 in sorted(list1)[::-1][:5]:
    rub = int(list2)
    kop = (list2 - rub) * 100
    list3.append(f'{rub:02} руб. {kop:02.0f} коп.')
list4 = ', '.join(list3)
print(list4)
