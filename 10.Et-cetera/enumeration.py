# Task is to count the number of students in the list and print there names alongside


# Way without using "enumeration".
def main():
    students = ["gyan", "dev", "sharma"]

    for i in range(len(students)):
        print(i + 1, students[i])


main()


# We can change above code using enumeration.
# We do enumeration using "enumerate" class.
# Enumeration ----> to name things separately, one by one
def main1():
    students = ["gyan", "dev", "sharma"]

    for i, student in enumerate(students, 1):
        print(i, student)


main1()

""" Syntax: 
    enumerate(iterable, start=0)
Parameters:
    Iterable: any object that supports iteration
    Start: the index value from which the counter is to be started, by default it is 0
 """

# "enumarate" class returns a object.Which can we converted to dictionary or list or can be iterate
# using for loop

# go to https://www.geeksforgeeks.org/enumerate-in-python/ to learn more about enumeration.
