def main():
    with open("7.File_IO\\name.txt", "r") as file:
        for line in sorted(file, key=len):
            print("Hello,", line.rstrip())


if __name__ == "__main__":
    main()
