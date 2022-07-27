import numpy
import time

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
    result = numpy.prod(x)*discount_decimal
    print(round(result, 2))


while True:
    try:
        if operations == 1:
            prices = price1 = float(input("Product_price> "))
            print()
            discount_percentage = int(input("Discount percentage > "))
            subtracted_value = 100-discount_percentage
            discount_decimal = subtracted_value/100
            print()
            print(f'Price after discount ({discount_percentage}%)')
            calculate(price1)

        elif operations == 2:
            prices = price1 = float(input("Product1_price> "))
            price2 = float(input("Product2_price> "))
            prices = price1+price2
            print()
            discount_percentage = int(input("Discount percentage > "))
            subtracted_value = 100-discount_percentage
            discount_decimal = subtracted_value/100
            print()
            print(f'Prices after discount ({discount_percentage}%)')
            calculate(price1)
            calculate(price2)

        elif operations == 3:
            prices = price1 = float(input("Product1_price> "))
            price2 = float(input("Product2_price> "))
            price3 = float(input("Product3_price> "))
            print()
            discount_percentage = int(input("Discount percentage > "))
            subtracted_value = 100-discount_percentage
            discount_decimal = subtracted_value/100
            print()
            print(f'Prices after discount ({discount_percentage}%)')
            calculate(price1)
            calculate(price2)
            calculate(price3)

        elif operations == 4:
            prices = price1 = float(input("Product1_price> "))
            price2 = float(input("Product2_price> "))
            price3 = float(input("Product3_price> "))
            price4 = float(input("Product4_price> "))
            print()
            discount_percentage = int(input("Discount percentage > "))
            subtracted_value = 100-discount_percentage
            discount_decimal = subtracted_value/100
            print()
            print(f'Prices after discount ({discount_percentage}%)')
            calculate(price1)
            calculate(price2)
            calculate(price3)
            calculate(price4)

        elif operations == 5:
            prices = price1 = float(input("Product1_price> "))
            price2 = float(input("Product2_price> "))
            price3 = float(input("Product3_price> "))
            price4 = float(input("Product4_price> "))
            price5 = float(input("Product5_price> "))
            print()
            discount_percentage = int(input("Discount percentage > "))
            subtracted_value = 100-discount_percentage
            discount_decimal = subtracted_value/100
            print()
            print(f'Prices after discount ({discount_percentage}%)')
            print()
            calculate(price1)
            calculate(price2)
            calculate(price3)
            calculate(price4)
            calculate(price5)

    except ValueError:
        print('Invalid input')
    else:
        break

time.sleep(999)
