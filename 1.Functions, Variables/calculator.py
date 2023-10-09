# x,y=9,10
# print(x+y)

# taking integer input
# x=int(input("Enter x : "))
# y=int(input("Enter y : "))

# taking float input
x = float(input("Enter x : "))
y = float(input("Enter y : "))

# z=round(x+y)

z = x / y
print(f"{z:.2f}")  # .2f means decimal ke baad 2 number

z = 1000000
print(f"{z:,}")  # --> put comma after every 3 zeros from right to left.
