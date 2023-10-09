def main():
    # 1st way to retrieve values from csv file

    # with open("harry_potter.csv") as file:
    #     for line in sorted(file):
    #         row=line.rstrip().split(",")
    #         print(f"{row[0]} is in {row[1]}")

    # 2nd way to retrieve values from csv file using "list"

    # students=list()
    # with open("harry_potter.csv") as file:
    #     for line in file:
    #         name,house=line.rstrip().split(",")
    #         students.append(f"{name} is in {house}")

    # for student in students:
    #     print(student)

    # 3rd way to retrieve values from csv file using "dictionary"
    students = list()
    with open("harry_potter.csv") as file:
        for line in file:
            student = {}
            name, house = line.rstrip().split(",")
            student = {"name": name, "house": house}
            students.append(student)

    for student in students:
        print(f"{student['name']} is in {student['house']}")


if __name__ == "__main__":
    main()
