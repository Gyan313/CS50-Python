# 1st way
def main1():
    while True:
        try:
            x=int(input("value of x = "))
            break
        except ValueError:
            print("x is not integer")
    print(f"x is {x}")
# main1()

# 2nd way
def main2():
    while True:
        try:
            x=int(input("value of x = "))
        except ValueError:
            print("x is not integer")
        else:
            break
    print(f"x is {x}")
main2()