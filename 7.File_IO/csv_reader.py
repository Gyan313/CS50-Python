import csv


def main():
    students = []

    with open("harry_potter.csv") as file:
        reader = csv.reader(file)
        for name, house in reader:
            students.append({"name": name, "house": house})

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is in {student['house']}")


if __name__ == "__main__":
    main()


# harry_potter.csv

""" 
Name,House
Harry,"slytherine,Griffindor"
Harmaoni,Griffindor
Ron,Griffindor
"""
