def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    Grand_total = 0
    while True:
        try:
            Item = input("Item: ").title()
            Grand_total += total(menu, Item)
            print(f"Total: ${Grand_total:.2f}")
        except KeyError:
            pass
        except EOFError:
            # this exception is raised when you give control + z as input
            break


def total(menu, Item):
    return menu[Item]


main()
