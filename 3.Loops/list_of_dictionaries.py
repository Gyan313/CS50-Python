def main():
    students=[
        {"name":"Harry","house":"Grifindor","patronous":"stag"},
        {"name":"Harmanoi","house":"Grifindor","patronous":"otter"},
        {"name":"Ron","house":"Grifindor","patronous":"weasle"},
        {"name":"Draco","house":"Slythrine","patronous":None},
    ]

    print(students[1]["name"])
    for student in students:
        print(student["name"],student["house"],student["patronous"],sep=" , ")
main()