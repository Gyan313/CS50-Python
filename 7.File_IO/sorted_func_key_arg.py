def main():
    students=list()

    with open("7.File_IO\harry_potter.csv") as file:
        for line in file:
            student={}
            name,house=line.rstrip().split(",")
            student={"name":name,"house":house}
            students.append(student)

        # def get_name(student):
        #     return student["name"]
        
        for student in sorted(students,key=lambda student:student["name"]): #using lamda to make anonymous function
            print(f"{student['name']} is in {student['house']}")

if __name__=="__main__":
    main()