def main():
    name=input("What is your name?")
    # open function : mode=writing
    with open("name.txt","a") as file:
        file.write(f"{name}\n")

if __name__=="__main__":
    main()