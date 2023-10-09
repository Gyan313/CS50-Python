def main():
    x=get_x("value of x : ")
    print(f"x is {x}")

def get_x(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()