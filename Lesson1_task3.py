# Грибов Алексей nynblpka@gmail.com

percents = int(input('Введите проценты: '))
last_digit = int(str(percents)[-1])
if percents == 11:
    word = 'процентов'
elif percents == 12:
    word = 'процентов'
elif percents == 13:
    word = 'процентов'
elif percents == 14:
    word = 'процентов'
elif last_digit == 1:
    word = 'процент'
elif last_digit == 2:
    word = 'процента'
elif last_digit == 3:
    word = 'процента'
elif last_digit == 4:
    word = 'процента'
else:
    word = 'процентов'
print(percents, word)
