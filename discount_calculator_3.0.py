import numpy
from numpy import prod
import time
from time import sleep

print()
while True:
    try:
        operations = int(
            input('How many products do you want to calculate ? (maximum of 5) > '))
        if operations <= 0:
            print('Invalid number of operations')
        elif operations > 5:
            print('Limit of operations surpassed')
        else:
            break
    except ValueError:
        print('Invalid input')

print()
print("Products:")
print()
input()
print()


def calculate(x):
    result = prod(x)*discount
    print(round(result, 2))
    return(result)


def calculate_savings(y, z):
    economized_value = y-z
    print(round(economized_value, 2))


def ask_for_discount():
    discount_percentage = int(input("Discount percentage > "))
    subtracted_value = 100-discount_percentage
    discount_decimal = subtracted_value/100
    return(discount_decimal)


while True:
    try:
        if operations == 1:
            price1 = float(input("Product_price> "))
            print()
            discount = ask_for_discount()
            print()
            print("Price after discount:")
            result1 = calculate(price1)
            print("Amount saved:")
            calculate_savings(price1, result1)

        elif operations == 2:
            price1 = float(input("Product1_price> "))
            price2 = float(input("Product2_price> "))
            prices = price1 + price2
            print()
            discount = ask_for_discount()
            print()
            print("Prices after discount:")
            result1 = calculate(price1)
            result2 = calculate(price2)
            results = result1 + result2
            print("Amount saved:")
            calculate_savings(prices, results)

        elif operations == 3:
            price1 = float(input("Product1_price> "))
            price2 = float(input("Product2_price> "))
            price3 = float(input("Product3_price> "))
            prices = price1 + price2 + price3
            print()
            discount = ask_for_discount()
            print()
            print("Prices after discount:")
            result1 = calculate(price1)
            result2 = calculate(price2)
            result3 = calculate(price3)
            results = result1 + result2 + result3
            print("Amount saved:")
            calculate_savings(prices, results)

        elif operations == 4:
            prices = price1 = float(input("Product1_price> "))
            price2 = float(input("Product2_price> "))
            price3 = float(input("Product3_price> "))
            price4 = float(input("Product4_price> "))
            prices = price1 + price2 + price3 + price4
            print()
            discount = ask_for_discount()
            print()
            print("Prices after discount:")
            result1 = calculate(price1)
            result2 = calculate(price2)
            result3 = calculate(price3)
            result4 = calculate(price4)
            results = result1 + result2 + result3 + result4
            print("Amount saved:")
            calculate_savings(prices, results)

        elif operations == 5:
            price1 = float(input("Product1_price> "))
            price2 = float(input("Product2_price> "))
            price3 = float(input("Product3_price> "))
            price4 = float(input("Product4_price> "))
            price5 = float(input("Product5_price> "))
            prices = price1 + price2 + price3 + price4 + price5
            print()
            discount = ask_for_discount()
            print()
            print("Prices after discount:")
            result1 = calculate(price1)
            result2 = calculate(price2)
            result3 = calculate(price3)
            result4 = calculate(price4)
            result5 = calculate(price5)
            results = result1 + result2 + result3 + result4 + result5
            print("Amount saved:")
            calculate_savings(prices, results)

    except ValueError:
        print('Invalid input')
    else:
        break

sleep(999)
