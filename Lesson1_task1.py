# Грибов Алексей nynblpka@gmail.com

dur = int(input('Введите промежуток времени в секундах: '))
day = dur // (60 * 60 * 24)
hour = (dur - (day * 60 * 60 * 24)) // (60 * 60)
min = (dur - ((day * 60 * 60 * 24) + (hour * 60 * 60))) // 60
sec = (dur - ((day * 60 * 60 * 24) + (hour * 60 * 60) + (min * 60)))
if hour == 0 and day == 0 and min == 0:
    print(sec, 'сек.')
elif hour == 0 and day == 0:
    print(min, 'мин.', sec, 'сек.')
elif day == 0:
    print(hour, 'ч.', min, 'мин.', sec, 'сек.')
else:
    print(day, 'дн.', hour, 'ч.', min, 'мин.', sec, 'сек.')