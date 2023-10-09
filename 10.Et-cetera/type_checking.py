# We do type checking using 2 things --->
# 1) mypy
# 2) type Hints(different for functions(->) and variables(:))

# Notes---->
# When you make a variable in language like c++, you declare data type with variable explicitly
#  wheather it is "int" or "str", so if you enter value of some other data type in int variable
# than c++ tells you right there that this assaignment is wrong before even running program.

# But you see in python it is not like that you can assaign a variable any data type value cause
# python assaign data type to the variable according to the value assaigned dynmically(implicitly)
# not statically(explicitly).

# Thats why python introduced something called "type hint" and "mypy" to check if we are giving variables
# value they are intended to have.

# How to use type hint??
# Type hint ---> to apply type hint do ... <variable_name>: dataType
#                               above dataType after ":" is what you want variable to have.
# Ex.. of 'type hint' below --> fib(n: int) and (number: int)


# mypy --->  is a Type checker that help ensure that you’re using variables and functions in your
#            code correctly.
# "mypy" will follow your given "type hint" as soon as it ecounters the first type hint gets
# voilated ,a error will be produced.
# Mypy is a static checker, so it finds bugs in your programs without even running them!

# How to use mypy?
#    1) install it via ---> pip install mypy
#    2) use it in terminal , type ---> mypy <program_name>.py

# Thats why mypy is for the programmers because users not gonna run mypy check on the program.
# As python doesnt warn us before user runs the code like c++, mypy will be a great tool for us.

# Remember, mypy and typeHints doesnt solve the problems they just tell us wheres the problem at.
# IT's our work to solve the problem.


def main():
    def fib(n: int):
        if n == 0:
            return 0
        elif n == 1:
            return 1

        return fib(n - 1) + fib(n - 2)

    number: int = input("enter the number: ")
    fib(number)


# main()

# There's gonna be an error on line 44 when you run code with "mypy" as there is a typeHint in place
# telling us that number variable must be {'int'} but we are assaigning it with "{str}".


def main1():
    number: int = int(input("Number: "))
    Meow: str = meow(number)
    print(Meow)


def meow(n: int) -> None:  # --> here "->None" means function meow(n) returns "None"
    for _ in range(n):
        print("meow")


""" 
Output: 
    Number: 2
    meow
    meow
    None
"""

# see above what happens when you input  "number=2", on line 56 meow(n) funtion is called that prints
# 2 times meow but see meow(n) doesnt return anything means it returns "none", that none got
# assaigned to "Meow" variable (see on line 56), thats why in above output you see "None" in last.

# Meaning on line (Meow: str = meow(number)) we are assaigning a function that returns "None" to the
# str expecting variable.
# We can fix that with assaigning the function meow(n) with typeHint "-> None".
# We apply "->" when we want to specify that our typeHint returns this or that.
# Ex ----> def meow(n)->None , def meow(n) -> str etc.

# After applying this "-> type" to a function we can use mypy to check for errors where we apply
# typeHints.

main1()
