# Грибов Алексей nynblpka@gmail.com

list_1 = []
for num in range(1, 1001, 2):
    list_1.append(num ** 3)
print(list_1)

total_sum = 0
for num in list_1:
    cube_sum = 0
    for cube_num in str(num):
        cube_sum += int(cube_num)
    if cube_sum % 7 == 0:
        total_sum += num
print(total_sum)

total17_sum = 0
for num in list_1:
    num += 17
    sum_17 = 0
    for num_17 in str(num):
        sum_17 += int(num_17)
    if sum_17 % 7 == 0:
        total17_sum += num
print(total17_sum)
