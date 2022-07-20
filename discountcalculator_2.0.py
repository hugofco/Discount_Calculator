import numpy
import time

# comments if i forget the meaning of some variables:
# p1 = price1, ev = economized value, dp = Discount percentage,
# ras = remaining after subtraction, fo = final operator

print()
while True:
    operations = int(
        input('How many products do you want to calculate ? (maximum of 5) > '))
    if operations > 0:
        if operations < 6:
            break

print()
print("Products:")
print()
input()
print()

if operations == 1:
    Prices = p1 = float(input("Product_price> "))
    print()
    Dp = int(input("Discount percentage > "))
    ras = 100-Dp
    Fo = ras/100
    print()
    print('Price after discount:')
    result = numpy.prod(Prices)*Fo
    print(round(result, 2))
    ev = Prices-result
    print("Amount Saved:")
    print(round(ev, 2))

elif operations == 2:
    Prices = p1 = float(input("Product1_price> "))
    p2 = float(input("Product2_price> "))
    print()
    Dp = int(input("Discount percentage > "))
    ras = 100-Dp
    Fo = ras/100
    print()
    print('Prices after discount:')
    result1 = numpy.prod(p1)*Fo
    print(round(result1, 2))
    result2 = numpy.prod(p2)*Fo
    print(round(result2, 2))
    ev1 = p1-result1
    ev2 = p2-result2
    print("Amount Saved:")
    print(round(ev1+ev2, 2))

elif operations == 3:
    Prices = p1 = float(input("Product1_price> "))
    p2 = float(input("Product2_price> "))
    p3 = float(input("Product3_price> "))
    print()
    Dp = int(input("Discount percentage > "))
    ras = 100-Dp
    Fo = ras/100
    print()
    print('Prices after discount:')
    result1 = numpy.prod(p1)*Fo
    print(round(result1, 2))
    result2 = numpy.prod(p2)*Fo
    print(round(result2, 2))
    result3 = numpy.prod(p3)*Fo
    print(round(result3, 2))
    ev1 = p1-result1
    ev2 = p2-result2
    ev3 = p3-result3
    print("Amount Saved:")
    print(round(ev1+ev2+ev3, 2))

elif operations == 4:
    Prices = p1 = float(input("Product1_price> "))
    p2 = float(input("Product2_price> "))
    p3 = float(input("Product3_price> "))
    p4 = float(input("Product4_price> "))
    print()
    Dp = int(input("Discount percentage > "))
    ras = 100-Dp
    Fo = ras/100
    print()
    print('Prices after discount:')
    result1 = numpy.prod(p1)*Fo
    print(round(result1, 2))
    result2 = numpy.prod(p2)*Fo
    print(round(result2, 2))
    result3 = numpy.prod(p3)*Fo
    print(round(result3, 2))
    result4 = numpy.prod(p4)*Fo
    print(round(result4, 2))
    ev1 = p1-result1
    ev2 = p2-result2
    ev3 = p3-result3
    ev4 = p4-result4
    print("Amount Saved:")
    print(round(ev1+ev2+ev3+ev4, 2))

elif operations == 5:
    Prices = p1 = float(input("Product1_price> "))
    p2 = float(input("Product2_price> "))
    p3 = float(input("Product3_price> "))
    p4 = float(input("Product4_price> "))
    p5 = float(input("Product5_price> "))
    print()
    Dp = int(input("Discount percentage > "))
    ras = 100-Dp
    Fo = ras/100
    print()
    print('Prices after discount:')
    result1 = numpy.prod(p1)*Fo
    print(round(result1, 2))
    result2 = numpy.prod(p2)*Fo
    print(round(result2, 2))
    result3 = numpy.prod(p3)*Fo
    print(round(result3, 2))
    result4 = numpy.prod(p4)*Fo
    print(round(result4, 2))
    result5 = numpy.prod(p5)*Fo
    print(round(result5, 2))
    ev1 = p1-result1
    ev2 = p2-result2
    ev3 = p3-result3
    ev4 = p4-result4
    ev5 = p5-result5
    print("Amount Saved:")
    print(round(ev1+ev2+ev3+ev4, 2))

time.sleep(999)
