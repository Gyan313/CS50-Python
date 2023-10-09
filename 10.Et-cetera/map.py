# map in python


# main2() is done without using map in python
def main2():
    yell("this", "is", "Gyan")


def yell(*words):
    # (*words) same as (*args) can accept any no. of positional arguments.
    uppercase = []
    for word in words:
        uppercase.append(word.upper())
    print(
        *uppercase
    )  # --> unpacking the list uppercase inside the print().But you can't perform
    #                        unpacking in fstring.


# main2()

# LEts use map to do the same thing as above main2() function.But map will do it in tighter and
# less code writing way


def main3():
    yell("this", "is", "Dev")


def yell(*words):
    # (*words) same as (*args) can accept any no. of positional arguments.
    uppercase = map(str.upper, words)  # this is how we use map
    # str.upper ---> upper is the funtion of str.
    # (*words) --> is a tuple.
    print(*uppercase)
    # --> unpacking the list uppercase inside the print().But you can't perform
    #     unpacking in fstring.

    # map --->
    # map(fun, iter) ---> syntax of how to make map object.
    # here function part dont need () just the name of the function.
    # EX ---> map(str.upper,list) not map(str.upper(),list)
    #           How does "map" work??
    # "map" passes each value of the given "iterator" through the given "function" and then return
    # the list of what function returns for each value of the iterator.


main3()
