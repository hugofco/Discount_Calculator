import numpy
# Product list:
# potatoes, tomatoes, toilet paper, broom, eggs;

a = "potatoes"
b = "tomatoes"
c = "toilet_paper"
d = "broom"
e = "eggs"

product_list = a, b, c, d, e

# product codes

A001 = a
B002 = b
C003 = c
D004 = d
E005 = e

code_list = ["A001", "B002", "C003", "D004", "E005"]

# listadepreços

A001_price = 8.78
B002_price = 5.79
C003_price = 12.79
D004_price = 17.98
E005_price = 9.99

price_list = [A001_price, B002_price, C003_price, D004_price, E005_price]

# discount = 27%
# final price = 100 - Discount =
Discount = 0.73
Discount_percentage = '27%'

# resposta final:
print('Product Code:')
print('                  ')
print(code_list)
print('                  ')
print('Product List:')
print('                  ')
print(product_list)
print('                  ')
print('Prices(in respective order):')
print('                  ')
print(price_list)
print('                  ')
print(f'Prices after discount ({Discount_percentage}) respectively:')

Price1 = A001_price
result1 = numpy.prod(A001_price)*Discount
print(result1)

Price2 = B002_price
result2 = numpy.prod(B002_price)*Discount
print(result2)

Price3 = C003_price
result3 = numpy.prod(C003_price)*Discount
print(result3)

Preço4 = D004_price
result4 = numpy.prod(D004_price)*Discount
print(result4)

Price5 = E005_price
result5 = numpy.prod(E005_price)*Discount
print(result5)
