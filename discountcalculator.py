import numpy
import time

operations = int(
    input('How many products do you want to calculate ? (maximum of 5) > '))
print('')
print("Write down the name of the products:")
print('')

# list of products

PRODUCTS_list = input("Products > ")
print('')

# price list:

if 1 == operations:
    Price1 = float(input("Product1_price > "))
    PRICES_list = Price1

if 2 == operations:
    Price1 = float(input("Product1_price > "))
    Price2 = float(input("Product2_price > "))
    PRICES_list = Price1, Price2

if 3 == operations:
    Price1 = float(input("Product1_price > "))
    Price2 = float(input("Product2_price > "))
    Price3 = float(input("Product3_price > "))
    PRICES_list = Price1, Price2, Price3

if 4 == operations:
    Price1 = float(input("Product1_price > "))
    Price2 = float(input("Product2_price > "))
    Price3 = float(input("Product3_price > "))
    Price4 = float(input("Product4_price > "))
    PRICES_list = Price1, Price2, Price3, Price4

if 5 == operations:
    Price1 = float(input("Product1_price > "))
    Price2 = float(input("Product2_price > "))
    Price3 = float(input("Product3_price > "))
    Price4 = float(input("Product4_price > "))
    Price5 = float(input("Product5_price > "))
    PRICES_list = Price1, Price2, Price3, Price4, Price5

# discount = value inserted by user

# final price = 100 - Discount divided by 100

print('')
Discount_percentage = int(input("Discount_value > "))

Discount_value = 100 - Discount_percentage

Final_discount_value = Discount_value/100

# results

if operations == 1:
    result1 = numpy.prod(Price1)*Final_discount_value

if operations == 2:
    result1 = numpy.prod(Price1)*Final_discount_value
    (round(result1, 2))
    result2 = numpy.prod(Price2)*Final_discount_value
    print(round(result2, 2))

if operations == 3:
    result1 = numpy.prod(Price1)*Final_discount_value
    result2 = numpy.prod(Price2)*Final_discount_value
    result3 = numpy.prod(Price3)*Final_discount_value

if operations == 4:
    result1 = numpy.prod(Price1)*Final_discount_value
    result2 = numpy.prod(Price2)*Final_discount_value
    result3 = numpy.prod(Price3)*Final_discount_value
    result4 = numpy.prod(Price4)*Final_discount_value

if operations == 5:
    result1 = numpy.prod(Price1)*Final_discount_value
    result2 = numpy.prod(Price2)*Final_discount_value
    result3 = numpy.prod(Price3)*Final_discount_value
    result4 = numpy.prod(Price4)*Final_discount_value
    result5 = numpy.prod(Price5)*Final_discount_value

# final answer:

print('')
print('Product List:')
print('')
print(PRODUCTS_list)
print('')
print('Prices(in respective order):')
print('')
print(PRICES_list)
print('')
print(f'Prices after discount ({Discount_percentage}%) respectively:')
print('')

if operations == 1:
    print(round(result1, 2))

elif operations == 2:
    print(round(result1, 2))
    print(round(result2, 2))

elif operations == 3:
    print(round(result1, 2))
    print(round(result2, 2))
    print(round(result3, 2))

elif operations == 4:
    print(round(result1, 2))
    print(round(result2, 2))
    print(round(result3, 2))
    print(round(result4, 2))

elif operations == 5:
    print(round(result1, 2))
    print(round(result2, 2))
    print(round(result3, 2))
    print(round(result4, 2))
    print(round(result5, 2))

time.sleep(999)
