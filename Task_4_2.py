
import requests


def currency_rates(cur):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    cur = cur.upper()
    if cur not in response:
        return

    name = response[response.find('<Name>', response.find(cur)) + 6:response.find('</Name>', response.find(cur))]
    rub = response[response.find('<Value>', response.find(cur)) + 7:response.find('</Value>', response.find(cur))]
    date = response[response.find('Date="') + 6:response.find('" name=')]
    return f'1 {name} = {rub} руб , {date}г.'


print(currency_rates('gbp'))
print(currency_rates('Usd'))
print(currency_rates('EUR'))
