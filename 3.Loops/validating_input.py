# we want to take input of a positive integer from a user, below while loop make sure of that.
while True:  # --> infinite loop
    n = int(input("n = "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
