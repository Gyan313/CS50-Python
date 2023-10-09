# In both list and dictionay comprehension value to be added is on the left and for loop condn vaghera
# on the right.


def main():
    students = ["gyan", "dev", "sharma"]

    griffindors = [{"name": student, "house": "griffindors"} for student in students]
    # This is how we make list of dictionaries using list comprehensions

    print(griffindors)


# main()


# dictionary comprehension -->
def main1():
    students = ["gyan", "dev", "sharma"]

    # pure dictionary comprehension same as list
    griffindors = {student: "Griffindor" for student in students}

    print(griffindors)


main1()
