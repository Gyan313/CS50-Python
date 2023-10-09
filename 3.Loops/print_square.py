def main():
    n=int(input("Side of square = "))
    print_square(n)

'''     
without nested loop
def print_square(size):
    for _ in range(size):
        print_column(size)

def print_column(n):
    print("#"*n)   
'''

# nested for loop
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#",end="")
        print()
main()