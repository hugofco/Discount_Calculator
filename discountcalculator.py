import numpy
import time
# Product list:
# potatoes, tomatoes, toilet paper, broom, eggs;

print("Write down the name of the products (maximum of 5 )")

a = input("Product1 > ")
b = input("Product2 > ")
c = input("Product3 > ")
d = input("Product4 > ")
e = input("Product5 > ")

product_list = a, b, c, d, e

# product codes

A001 = a
B002 = b
C003 = c
D004 = d
E005 = e

code_list = ["A001", "B002", "C003", "D004", "E005"]

# listadepreços

A001_price = float(input("Product1_price > "))
B002_price = float(input("Product2_price > "))
C003_price = float(input("Product3_price > "))
D004_price = float(input("Product4_price > "))
E005_price = float(input("Product5_price > "))

price_list = [A001_price, B002_price, C003_price, D004_price, E005_price]

# discount = 27%
# final price = 100 - Discount =
Discount = int(input("Discount_value > "))
Discount2 = 100 - Discount
Final_discount_value = Discount2/100
# final response:


print('                  ')
print('Product List:')
print('                  ')
print(product_list)
print('                  ')
print('Prices(in respective order):')
print('                  ')
print(price_list)
print('                  ')
print(f'Prices after discount ({Discount}%) respectively:')

Price1 = A001_price
result1 = numpy.prod(A001_price)*Final_discount_value
print(round(result1, 2))

Price2 = B002_price
result2 = numpy.prod(B002_price)*Final_discount_value
print(round(result2, 2))

Price3 = C003_price
result3 = numpy.prod(C003_price)*Final_discount_value
print(round(result3, 2))

Preço4 = D004_price
result4 = numpy.prod(D004_price)*Final_discount_value
print(round(result4, 2))

Price5 = E005_price
result5 = numpy.prod(E005_price)*Final_discount_value
print(round(result5, 2))

time.sleep(999)
