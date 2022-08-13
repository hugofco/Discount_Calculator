# Discount_Calculator
A simple application created with Numpy, which aims to get a list of products and execute the following tasks: display the list itself, the original prices of the products, their prices after a certain discount, and the amount saved after the discount.

# NumPy
NumPy is a library that provides more complex mathematical operations, if you need to execute some tasks that the integraded operations can't handle, or define larger math functions without having to write extensive amounts of code.

```python
from numpy inport prod

def calculate(x):
    result = prod(x)*discount
    print(round(result, 2))
    return(result)
```
This project used the numpy product function (numpy.prod), and as the name sugests, it's a function that can pick up an int or float value, (it can be a fixed value on the lines of code, or a value carried by a variable), and then calculate and return the result of the multiplications between these values (product). As shown on the example above.


# How to run:
(Recomended to replicate on a new virtual enviorment).

* Download, or copy and paste the source code file (discountcalculator.py) just make sure that the file you pasted the code have the same name.

(or just use git clone if you're used to)

# <h3> Setting up a new virtual enviorment:
 
* Open a new terminal window and execute the following commands:



```shell
python -m venv name
name/scripts/activate
```
* Your terminal will indicate the activation of your new enviorment 

```shell
(name) PS C:\Users\Desktop\YourFolder>
```
# <h3> Running the application:
 
* Then, execute this command lines on your new environment:

```shell
pip install numpy
python discountcalculator.py
```
