def main():
    x=int(input("enter the value of x: "))
    print(f"Square of {x} is {square(x)}")

def square(x):
    # return x**2
    return pow(x,2)

main()