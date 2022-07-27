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
            result = numpy.prod(prices)*discount_decimal
            print(round(result, 2))
            economized_value = prices-result
            print("Amount Saved:")
            print(round(economized_value, 2))

        elif operations == 2:
            prices = price1 = float(input("Product1_price> "))
            price2 = float(input("Product2_price> "))
            print()
            discount_percentage = int(input("Discount percentage > "))
            subtracted_value = 100-discount_percentage
            discount_decimal = subtracted_value/100
            print()
            print(f'Prices after discount ({discount_percentage}%)')
            result1 = numpy.prod(price1)*discount_decimal
            print(round(result1, 2))
            result2 = numpy.prod(price2)*discount_decimal
            print(round(result2, 2))
            economized_value1 = price1-result1
            economized_value2 = price2-result2
            print("Amount Saved:")
            print(round(economized_value1+economized_value2, 2))

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
            result1 = numpy.prod(price1)*discount_decimal
            print(round(result1, 2))
            result2 = numpy.prod(price2)*discount_decimal
            print(round(result2, 2))
            result3 = numpy.prod(price3)*discount_decimal
            print(round(result3, 2))
            economized_value1 = price1-result1
            economized_value2 = price2-result2
            economized_value3 = price3-result3
            print("Amount Saved:")
            print(round(economized_value1+economized_value2+economized_value3, 2))

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
            result1 = numpy.prod(price1)*discount_decimal
            print(round(result1, 2))
            result2 = numpy.prod(price2)*discount_decimal
            print(round(result2, 2))
            result3 = numpy.prod(price3)*discount_decimal
            print(round(result3, 2))
            result4 = numpy.prod(price4)*discount_decimal
            print(round(result4, 2))
            economized_value1 = price1-result1
            economized_value2 = price2-result2
            economized_value3 = price3-result3
            economized_value4 = price4-result4
            print("Amount Saved:")
            print(round(economized_value1+economized_value2 +
                  economized_value3+economized_value4, 2))

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
            result1 = numpy.prod(price1)*discount_decimal
            print(round(result1, 2))
            result2 = numpy.prod(price2)*discount_decimal
            print(round(result2, 2))
            result3 = numpy.prod(price3)*discount_decimal
            print(round(result3, 2))
            result4 = numpy.prod(price4)*discount_decimal
            print(round(result4, 2))
            result5 = numpy.prod(price5)*discount_decimal
            print(round(result5, 2))
            economized_value1 = price1-result1
            economized_value2 = price2-result2
            economized_value3 = price3-result3
            economized_value4 = price4-result4
            economized_value5 = price5-result5
            print("Amount Saved:")
            print(round(economized_value1+economized_value2 +
                  economized_value3+economized_value4+economized_value5, 2))

    except ValueError:
        print('Invalid input')
    else:
        break

time.sleep(999)
