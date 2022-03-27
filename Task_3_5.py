import random
# n - quanty jokes
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def getjokes (n):
    '''getjokes - repeat jokes n quanty with diffrent words'''
    for i in range(n):
        joke = [f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}']
        print(joke, end=' ')


getjokes(100)
