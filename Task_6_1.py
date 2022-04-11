file = open('logs.txt')

tuplec = []
for line in file:
    splitted = line.split()
    tuplec.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
print('\n'.join(map(str, tuplec)))
