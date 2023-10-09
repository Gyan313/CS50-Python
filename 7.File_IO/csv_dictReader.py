import csv


def main():
    students = []

    with open("harry_potter.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # students.append({'name':row["name"],'house':row["house"]})
            students.append(row)  # as row is a dictionary itself

    for student in sorted(students, key=lambda student: student["Name"]):
        print(f"{student['Name']} is in {student['House']}")


if __name__ == "__main__":
    main()
