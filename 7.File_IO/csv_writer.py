import csv

def main():
    name=input("Student's name: ")
    house=input("Student's house: ")
    with open("7.File_IO\harry_potter.csv","a") as file:
        writer=csv.writer(file)
        writer.writerow([name,house])


if __name__=="__main__":
    main()