def main():
    names = get_names()
    names = [name.title() for name in names]
    print("Adieu, adieu, to ", end="")
    if len(names) == 1:
        print(names[0])

    elif len(names) == 2:
        print(" and ".join(names))

    else:
        print(", ".join(names[:-1]) + f", and {names[-1]}")


def get_names() -> list[str]:
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break
    return names


if __name__ == "__main__":
    main()

# EOFError ----> press "control + Z".
# names[:-1] ----> from 1st element to 2nd last element of the list
# names[-1] -----> last element of the list
