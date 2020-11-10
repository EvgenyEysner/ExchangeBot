import requests
from struct import unpack
import json

keys = {'Доллар': 'USD', 'Евро': 'EUR', 'Рубль': 'RUB'}
msg = 'евро рубль 1'
for i in msg:
    print(list(i))

#quote, base, amout = values
#r = requests.get(f'https://api.exchangeratesapi.io/latest?base={keys[quote]}&symbols={keys[base]}')

#total_base = json.loads(r.content)['rates'][keys[base]]
print(values)


