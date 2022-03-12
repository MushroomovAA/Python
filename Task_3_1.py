# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"

def my_f(x):
    dictionary = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                  'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    print(dictionary.get(x))


my_f('one')
