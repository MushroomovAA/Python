from itertools import zip_longest

with open('Users.csv', encoding= 'utf-8') as f_users:
    users = []
    for line in f_users:
        users.append(line.strip().replace('"', ''))
with open('Hobby.csv', encoding= 'utf-8') as f_hobby:
    hobby = []
    for line in f_hobby:
        hobby.append(line.strip().replace('"', ''))

if len(users) > len(hobby):
    exit(1)

else:
    dict_zip = ((users, hobby) for users, hobby in zip_longest(users, hobby, fillvalue=None))
    print(dict(dict_zip))
