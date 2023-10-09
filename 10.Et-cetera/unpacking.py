# suppose we just want the first name of the user from the inputed full name by user.

""" 
    first, _ = input("Name: ").split(" ")
    print(f"hello, {first}") 
"""

# Here above when we split the inputed name by user, we just wanted first name so we only provided
# first variable and for second value of the splited name we just put "_" to show that we dont want
# to store this value anywhere.

# EX -->  "_=2" here 2 is stored in no variable.


# Unpacking containers of different kind.
def main():
    # Unpacking in "ordered elements" containing containers. Eg --> list etc.
    coins = [100, 50, 20]
    print(f"{total(100,50,20)} knuts")
    #          OR
    print(f"{total(*coins)} knuts")
    # Here coins is a list, so in order to unpack it we need to do (*coins).
    # (*list) -->thats how to unpack a list, what it do was unpack all the values of the
    # list. Like in case of *coins it will unpack all the values inside the list like this ---> 100,50,20
    # If coins=[1,2,3,4,5,6] than (*coins) will be ---> 1,2,3,4,5,6
    # Above we passed arguments to the total where each values position matters when passing to
    # to the total() funtion. Thus, these types of arguments are "positional arguments".

    # We can unpack elements of the dictionary using (**Dict) like list.Dictionaries dont need to
    #  be ordered.
    coinsDict = {"galleans": 100, "sickle": 50, "knuts": 20}
    # Below 2 prints are exactly same in what they do.Cause both dont need order to pass the arguments.
    # These type of arguments where we use name to pass the value like below (galleans=100,sickle=50,knuts=20)
    # are called "named arguments" in python.So (galleans=100) is a named argument and dont need to
    # passed in any specific order.
    print(f"{total(galleans=100,sickle=50,knuts=20)}")
    #       OR
    print(f"{total(**coinsDict)} knuts")
    # This print() is exactly same as above print() as **coins unpack into galleans=100,sickle=50,knuts=20
    # implicity by python.


def total(galleans, sickle, knuts):
    return (galleans * 16 + sickle) * 29 + knuts


# main()


# Pythonic way to handle positianal and nameed arguments.
def main1():
    # f(100, 29, 34, 44)  ---> position arguments passed and collected in *args in f() function parameter.

    f(gyan=100, srishti=100, mammi=100)
    l = [1, 2, 4]
    f(l)
    # Output : Positional:  ([1, 2, 4],)
    #          Named: {}

    # but if you do -->
    f(gyan=l)
    # output: Positional:  ()
    #         Named:  {'gyan': [1, 2, 4]}


def f(*args, **kwargs):
    print(
        "Positional: ", args
    )  # ---> to print positional arguments collected in *args.
    # Output --> Positional: (100,29,34,44). Output is a tuple here.

    print("Named: ", kwargs)  # ---> to print Named arguments collected in **kwargs
    # Output --> Named:  {'gyan': 100, 'srishti': 100, 'mammi': 100} . Output is a dictionary here.

    # You can pass values to both *args and **kwargs, but you need to pass values in function
    # carefully then. first pass the position arguments and then pass the named arguments.
    # EX ---> f(2,3,4,gyan=100)

    # print(*objects, sep=' ', end='\n', file=None, flush=False)
    # Look above in print() function we got a inbuilt (*object) this is indeed to collect the
    # positional arguments passed in the print().
    # But,sep=" " is a named argument and other too.

    # *args ---> here "args" can be of any name, "ex" --> *words, *coins same as *args.
    # same can be done for **kwargs


main1()
