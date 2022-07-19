import numpy
import time

while True:
    operations = int(
        input('How many products do you want to calculate ? (maximum of 5) > '))
    if operations > 0:
        if operations < 6:
            break

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

# Calculating percentage: 100 - (number typed by user), divided by 100

print('')
Discount_percentage = int(input("Discount_value > "))
Discount_value = 100 - Discount_percentage
Final_discount_value = Discount_value/100

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

# results
# ev = economized value

if operations == 1:
    result1 = numpy.prod(Price1)*Final_discount_value
    print(round(result1, 2))
    ev1 = Price1 - result1
    savings_list = ev1
    print('')
    print('Amount saved:')
    print('')
    print(round(savings_list, 2))

elif operations == 2:
    result1 = numpy.prod(Price1)*Final_discount_value
    print(round(result1, 2))
    result2 = numpy.prod(Price2)*Final_discount_value
    print(round(result2, 2))
    ev1 = Price1 - result1
    ev2 = Price2 - result2
    savings_list = ev1 + ev2
    print('')
    print('Amount saved:')
    print('')
    print(round(savings_list, 2))

elif operations == 3:
    result1 = numpy.prod(Price1)*Final_discount_value
    print(round(result1, 2))
    result2 = numpy.prod(Price2)*Final_discount_value
    print(round(result2, 2))
    result3 = numpy.prod(Price3)*Final_discount_value
    print(round(result3, 2))
    ev1 = Price1 - result1
    ev2 = Price2 - result2
    ev3 = Price3 - result3
    savings_list = ev1 + ev2 + ev3
    print('')
    print('Amount saved:')
    print('')
    print(round(savings_list, 2))

elif operations == 4:
    result1 = numpy.prod(Price1)*Final_discount_value
    print(round(result1, 2))
    result2 = numpy.prod(Price2)*Final_discount_value
    print(round(result2, 2))
    result3 = numpy.prod(Price3)*Final_discount_value
    print(round(result3, 2))
    result4 = numpy.prod(Price4)*Final_discount_value
    print(round(result4))
    ev1 = Price1 - result1
    ev2 = Price2 - result2
    ev3 = Price3 - result3
    ev4 = Price4 - result4
    savings_list = ev1 + ev2 + ev3 + ev4
    print('')
    print('Amount saved:')
    print('')
    print(round(savings_list, 2))

elif operations == 5:
    result1 = numpy.prod(Price1)*Final_discount_value
    print(round(result1, 2))
    result2 = numpy.prod(Price2)*Final_discount_value
    print(round(result2, 2))
    result3 = numpy.prod(Price3)*Final_discount_value
    print(round(result3, 2))
    result4 = numpy.prod(Price4)*Final_discount_value
    print(round(result4))
    result5 = numpy.prod(Price5)*Final_discount_value
    print(round(result5, 2))
    ev1 = Price1 - result1
    ev2 = Price2 - result2
    ev3 = Price3 - result3
    ev4 = Price4 - result4
    ev5 = Price5 - result5
    savings_list = ev1 + ev2 + ev3 + ev4 + ev5
    print('')
    print('Amount saved:')
    print('')
    print(round(savings_list, 2))

time.sleep(999)
