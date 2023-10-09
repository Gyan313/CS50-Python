balance = 0
# --> 'balance' is a global variable if we see from the below written function.

# You can only read a global variable but cannot change its value inside a function, if you try and
# and do that it will produce error.
# But if you insist on making global variable and you want update its value then you have to
# use global keyword in front of the variable. checkout below.


def main():
    print(f"Balance: {balance}")
    deposit(100)
    withdraw(50)
    print(f"Balance: {balance}")


def deposit(money):
    global balance  # ---> without declaring balance global first interpreter will think we are
    # using a variable without initilizing it to any data type .eg.. balance ="" or 0 etc.
    balance += money


def withdraw(money):
    global balance
    balance -= money


if __name__ == "__main__":
    main()

# donot make the same named local variable in a function if you are using global variable of same
# name in that function.
