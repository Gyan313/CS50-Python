def main():
    number=get_num()
    meow(number)

def get_num():
    while True:
        n=int(input("n = "))
        if n>0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()