
def thesaurus (*words):
    thesaurus = {}
    for word in words:
        firstlit = word[0].title()
        if firstlit not in thesaurus:
           thesaurus[firstlit] = []
        thesaurus[firstlit].append(word)
    print(thesaurus)


thesaurus('Иван', 'Илья', 'Мария', 'Петр', 'Петрушка', 'Маша', 'миша','данииЛ', 'Даша', 'Иося')