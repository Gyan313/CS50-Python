def main():
    with open("7.File_IO\\name.txt", "w") as file:
        file.write("Gyan\nSezal\nSharma")

    with open("7.File_IO\\name.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        print("Hello,", line.rstrip())


if __name__ == "__main__":
    main()
