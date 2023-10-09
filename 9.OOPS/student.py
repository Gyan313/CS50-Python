# What we are trying to do here---->
# We want to get student's name and age using just one funtion.
# for that we can use tuples,list and dictionaries, to return name and age in a single container.


def main():
    # --> recieving (multiple values) or tuple in the order they are returned.
    student = get_student()  # (or)    name,age = get_student
    print(f"{student[0]} - {student[1]} {student[2]}")
    # as i said tuples are immutable but still you can access them by using indexing like we did
    # above with student tuple


def get_student():
    name = input("Name: ")
    age = input("Age: ")

    return name, age  # -->  a tuple
    # in python you can return "multiple values" at same time using return keyword unlike other languages.
    # Actually this is syntax of "implicit tuple" to make this tuple explicit we need to enclose
    # these values in a circular paranthesis.
    # Ex ---> (name,age). And tuple is immutable meaning you cant change its value.


# main()


# When to use tuples??
# Ans) We use tuple when we want to store data which is needed not be changed in any way.
#      When you dont want data stored not to be changed.
# That means tuples can increase the correctness in your code and decrease probab of bugs in the
# code


# Using dictionaries
def main1():
    student = get_student()
    print(f"{student['name']} - {student['age']}")


def get_student():
    student = dict()
    student["name"] = input("Name: ")
    student["age"] = input("age: ")
    return student

    # Or

    """ 
    name = input("Name: ")
    age = input("Age: ")
    return {"name": name, "age": age} 
    """


# main1()


def main2():
    movies = ([1, 2, 3], [34, 3])

    # here we put list inside the tuple movies , and as we know list are mutable but tuple
    # immutable . So you can change the list inside the tuple.
    movies[0][0] = 2
    print(f"{movies}")


main2()
