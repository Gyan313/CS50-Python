# with open("harry_potter.csv", "a") as file:
#     file.writelines(
#         ["Harry,Griffindor,12", "Harmaoni,Griffindor,13", "Ron,Griffindor,14"]
#     )


""" 
with open("harry_potter.csv", "r") as file:
    students = []
    for line in file:
        name, house = line.strip().split(",")
        student = {
            "name": name,
            "house": house,
        }
        students.append(student)

    for student in sorted(students, key=lambda x: (x["name"])):
        print(student)
        
"""

import csv

""" student = []

with open("harry_potter.csv", "r") as file:
    reader = csv.DictReader(file)
    for name in reader:
        print(name)
 """
# Header of the csv file will implicitly become the keys of the dictionary created
# using csv.dictreader()


with open("harry_potter.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "House"])
    name = input("Name: ")
    house = input("House: ")
    writer.writerow({"name": name, "House": house})
