# x = '1,925.00'
# # y = int(x)

# number = x.split()[0].replace(',', '')
# print(type(number))
# print(number)

# nu = float(number)
# print(nu)
# print(type(nu))


# x = {'a':(1,2)}

# print(x['a'])
# print(list(x.keys())[0] == 'a')

# b = (1,2,3)

from file_gen import quote_symbol

quote_symbol.sort()

print(len(quote_symbol))
print(quote_symbol)
