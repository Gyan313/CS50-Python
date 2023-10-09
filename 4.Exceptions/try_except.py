def main():
    try:
        x=int(input("value of x = "))

    except ValueError:
        print("x in not integer")
    else:
        print(f"x = {x}")
    
main()