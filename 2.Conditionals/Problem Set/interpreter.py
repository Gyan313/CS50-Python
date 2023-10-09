# Program
expression = input("Expression: ")

x, y, z = expression.split(" ")

try:
    match (y):
        case "+":
            result = int(x) + int(z)
        case "-":
            result = int(x) - int(z)
        case "/":
            result = int(x) / int(z)
        case "*":
            result = int(x) * int(z)
        case _:
            pass

    # Using eval() function....
    # result = eval(expression)

    print(f"{float(result):.1f}")

except ZeroDivisionError:
    print("Warning: Division by zero, change your value of z.")
