list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

list2 = []
for num in list1:
    if num.isdigit():
        list2.extend(['"', f'{int(num):02}', '"'])
    elif num.startswith('+') and num[1:].isdigit():
        list2.extend(['"', f'{num[0]}{int(num[1:]):02}', '"'])
    else:
        list2.append(num)
list3 = ' '.join(list2)
print(list3)