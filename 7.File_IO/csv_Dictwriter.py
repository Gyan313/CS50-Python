import csv

def main():

    with open("7.File_IO\harry_potter.csv","a") as file:
        writer=csv.DictWriter(file,fieldnames=["name","house"])
        writer.writerow({"name":name,"house":house})

    name=input("Student's name: ")
    house=input("Student's house: ")

main()