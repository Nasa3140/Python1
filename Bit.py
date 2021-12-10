from forex_python.converter import CurrencyCodes, CurrencyRates
from forex_python.bitcoin import BtcConverter

test = CurrencyCodes()

cur_symbol = test.get_symbol('INR')
cur_name = test.get_currency_name('INR')


print('The currency name is : ' + cur_name);
print('The currency symbol is : ' + cur_symbol);

print('\n' + test.get_currency_name('USD'))
print(test.get_symbol('USD'))

test1 = CurrencyRates()

rate = test1.get_rate('USD', 'INR')

print(rate)

res = test1.convert('USD', 'INR', 10)

#print(res)

bitcoin = BtcConverter()

price = bitcoin.get_latest_price('INR')

print(price)