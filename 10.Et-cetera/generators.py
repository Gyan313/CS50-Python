# Below main() to show why we need generator function in python.
def main():
    n = int(input("Enter the n: "))
    lambs = lamb(n)
    for i in lambs:
        print(i)


def lamb(n):
    lambs = []
    for i in range(n):
        lambs.append("🐖" * i)
    return lambs


# let suppose in this function you pass n=1million what do you think will happen
# You will not get any answer as processor just cant do too much computation and stops.

# But above problem can handled using Generator functions in python.
# These functions are made using a keyword "yield" in place of "return".
# The functions containing "yield" are called generating function.
# By using "yield" now function returns one value at a time .This helps reducing the computation
# by processor at a single point of time.

# main()


# Below lamb(n) is a genertor function as it contain "yield" keyword.
def main1():
    n = int(input("Enter the n: "))
    lambs = lamb(n)
    for i in lambs:
        print(i)


def lamb(n):
    lambs = []
    for i in range(n):
        lambs.append("🐖" * i)
    yield lambs
    # here "yield" returns lambs list one element by one element.


# If the body of a def contains yield, the function automatically becomes a generator function.
main1()

# https://www.geeksforgeeks.org/generators-in-python/  ---> learn more about generator function.
