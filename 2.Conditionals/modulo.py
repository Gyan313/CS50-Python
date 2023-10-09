def main():
    x=int(input("Value of x : "))
    if is_even(x):
        print("Even number")
    else:
        print("odd number")


def is_even(x):
    '''
    if x%2==0:
        return True
    else:
        return False
    '''
    
    #              OR

    # return True if x%2==0 else False

    #              OR

    return x%2==0
main()