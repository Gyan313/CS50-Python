def main():
    directory = {}
    # step 1: Read and change the file and store it in a iterable
    with open("harry_potter.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            directory[name] = house

    directory["Harry"] = "slytherine"

    # step 2: open file to write the change text in it
    with open("harry_potter.csv", "w") as file:
        for i in directory:
            file.write(f"{i},{directory[i]}\n")


if __name__ == "__main__":
    main()
