def main():
    name=input("what is your name? ")

    match (name):
        case "Gyan" | "Dev" | "GD":
            print("he is the tech-entrepreneur")
        case "Srishti" | "Sharma" | "SS":
            print("She is the IAS officer")
        case _:
            print("I dont know about others")

main()