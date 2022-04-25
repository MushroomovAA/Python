import re
re_email = re.compile(r'^([a-zA-Z\d]+)@([a-zA-Z\d]+\.[a-zA-Z]+)$')


def email_parse(email):
    email_valid = re_email.findall(email)
    if email_valid:
        arg = email_valid[0]
    else:
        raise ValueError(f'invalid email: {email}')
    print(f'Username: {arg[0]}, Domain: {arg[1]}')


email_parse('mega@bolshoy.com')
