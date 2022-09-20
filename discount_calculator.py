from numpy import prod
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
input("Products: ")
print()


def calculate(*args):
    result = prod(args)*discount
    print(round(result, 2))
    return (result)


def calculate_savings(x, y):
    economized_value = x - y
    print(round(economized_value, 2))


def ask_for_discount():
    discount_percentage = int(input("Discount percentage > "))
    subtracted_value = 100-discount_percentage
    return (subtracted_value/100)


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
            print("Total before discount: ")
            print(round(prices, 2))
            print("Prices after discount:")
            results = calculate(prices)
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
            print("Total before discount: ")
            print(round(prices, 2))
            print("Prices after discount:")
            results = calculate(prices)
            print("Amount saved:")
            calculate_savings(prices, results)

        elif operations == 4:
            price1 = float(input("Product1_price> "))
            price2 = float(input("Product2_price> "))
            price3 = float(input("Product3_price> "))
            price4 = float(input("Product4_price> "))
            prices = price1 + price2 + price3 + price4
            print()
            discount = ask_for_discount()
            print()
            print("Total before discount: ")
            print(round(prices, 2))
            print("Prices after discount:")
            results = calculate(prices)
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
            print("Total before discount: ")
            print(round(prices, 2))
            print("Prices after discount:")
            results = calculate(prices)
            print("Amount saved:")
            calculate_savings(prices, results)

    except ValueError:
        print('Invalid input')
    else:
        break
sleep(999)
