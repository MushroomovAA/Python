# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

n = 16
odd_to_num = (num for num in range(1, n, 2))
print(next(odd_to_num))
print(next(odd_to_num))
print(next(odd_to_num))
print(next(odd_to_num))
print(next(odd_to_num))
print(next(odd_to_num))
print(next(odd_to_num))
print(next(odd_to_num))
print(next(odd_to_num))

