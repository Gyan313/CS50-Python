# This program is to show that global variable can be a soln to access modifier problem of python
# but it is not really a good way to write code as things could get messy while using global variable
# But with classes we can encapsulate all the data at one place and we will be fine with less bugs to resolve.


class Bank:
    def __init__(self):
        self._balance = 0

    @property  # --> way to define getter in python,so balance(self) is a getter.
    def balance(self):
        return self._balance

    # We didnt define setter here for our getter balance(self).

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Bank()
    print(f"Balance: {account.balance}")
    # account.balance   ---> call the property balance for us.

    # Look here "balance" is a property or getter and "_balance" is a instance variable.


main()
