def square(n: int):
    """
    This square(n)  funtion returns square of the given value of n

    :param n:Number to be squared
    :type n:int
    :raise TypeError:If n in not int
    :returns square of n
    :rtype:int
    """
    return n**2


# Above just below funtion signature we have our docstring for this function and a docstring must
# be eclosed in triple quotes.
# You see above wierd syntax of docstring, it is the syntax by convention.

number = int(input("Number: "))
Square = square(number)
print(Square)
print(
    square.__doc__
)  # --> __doc__ is the magic function to print the docstring of the sqaure function.

# Go here https://www.programiz.com/python-programming/docstrings to learn about doc string.

# Quick overview --->

# It is just a way to document a function so that a programmer dont have to document whole code
# after writing it, here the programmer can document there code with each function they make.
# This saves a lot of time.
# As after writing code and documenting in small-small parts there are funtions in python
# we can use to access the doc and manipulate it.
# Hell with using docString we can also find bugs in the function as one can pass sample input
# and outputs with docstring. Than we can use some python way to implement them on the respective
# function to check if they work or not.
# So, docstring is awesome.
