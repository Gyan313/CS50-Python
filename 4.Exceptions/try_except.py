# Used 'else' with try-except block....


def main():
    try:
        x = int(input("value of x = "))

    except ValueError:
        print("x in not integer")
    else:
        print(f"x = {x}")

    # if x is not integer UnboundLocalError will be raised cause x is not assaigned any value.
    # If no UnboundLocalError than you must have inputed string.
    print(x)


main()
