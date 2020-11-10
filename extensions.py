import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CurrencyConverter:
    def convert(quote: str, base: str, amout: float):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести две одинаковые валюты{base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amout = float(amout)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amout}')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={quote_ticker}&symbols={base_ticker}')
        total_base = json.loads(r.content)['rates'][keys[base]]

        return round(float(total_base), 2) * amout