from currency_converter import CurrencyConverter
from datetime import date

amt = int(input('enter amount to convert:'))
from_country = input('enter source currency:')

to_country = input('enter final currency:')

c = CurrencyConverter()
print(c.convert(amt,from_country,to_country))
